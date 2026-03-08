import re


def _extract_from_choice(choice):
    # try multiple nested locations for text/content
    if choice is None:
        return None
    # dict-like
    if isinstance(choice, dict):
        # delta > content
        delta = choice.get("delta")
        if isinstance(delta, dict) and delta.get("content"):
            return delta.get("content")
        if choice.get("text"):
            return choice.get("text")
        msg = choice.get("message")
        if isinstance(msg, dict) and msg.get("content"):
            return msg.get("content")
        return None

    # object-like
    text_attr = getattr(choice, "text", None)
    if text_attr:
        return text_attr
    delta = getattr(choice, "delta", None)
    if delta:
        if isinstance(delta, dict) and delta.get("content"):
            return delta.get("content")
        content = getattr(delta, "content", None)
        if content:
            return content
    msg = getattr(choice, "message", None)
    if msg:
        if isinstance(msg, dict) and msg.get("content"):
            return msg.get("content")
        mcontent = getattr(msg, "content", None)
        if mcontent:
            return mcontent
    return None


def _clean_text(s: str) -> str:
    """Trim and remove common repr/artifact characters from extracted text."""
    if not isinstance(s, str):
        return s
    # Preserve surrounding whitespace to avoid gluing tokens between chunks.
    s = s.replace("\x00", "")
    if not s:
        return s
    # Remove only leading/trailing punctuation characters (keep spaces)
    s = re.sub(r"^[\)\]\}'\",]+", "", s)
    s = re.sub(r"[\)\]\}'\",]+$", "", s)
    return s


def get_chunk_content(chunk, allow_repr_fallback: bool = False):
    """Normalize different chunk shapes into a plain string.

    Heuristics (best-effort):
    - If chunk is a plain string, return it.
    - If dict-like, look for `choices` -> `delta.content` / `text` / `message.content`.
    - If object with `choices`, prefer structured fields via `_extract_from_choice`.
    - Fallback to attributes `text`, `content`, `message` on the chunk.
    - As a last resort, parse the string repr and extract plaintext that often
      appears after an object repr (robust regex matching several known SDK names).
    """
    try:
        if isinstance(chunk, str):
            return _clean_text(chunk)

        # dict-like shapes
        if isinstance(chunk, dict):
            if "choices" in chunk and chunk["choices"]:
                val = _extract_from_choice(chunk["choices"][0])
                if val:
                    return _clean_text(val)
            # direct fields
            for k in ("content", "text", "data", "message"):
                v = chunk.get(k)
                if isinstance(v, str) and v.strip():
                    return _clean_text(v)
            return str(chunk)

        # object-like shapes
        choices = getattr(chunk, "choices", None)
        if choices:
            # choices may be generator-like; take first safely
            try:
                first = choices[0]
            except Exception:
                first = None
            val = _extract_from_choice(first)
            if val:
                return _clean_text(val)

        # common direct attributes
        for attr in ("text", "content", "data"):
            v = getattr(chunk, attr, None)
            if isinstance(v, str) and v.strip():
                return _clean_text(v)

        # message may be dict-like or object
        msg = getattr(chunk, "message", None)
        if msg:
            if isinstance(msg, dict) and msg.get("content"):
                return _clean_text(msg.get("content"))
            mcontent = getattr(msg, "content", None)
            if isinstance(mcontent, str) and mcontent.strip():
                return _clean_text(mcontent)

        # Last-resort: optionally parse string repr for plaintext appended after an object repr.
        if allow_repr_fallback:
            s = str(chunk)
            # Remove obvious control characters but preserve spacing
            s = s.replace("\x00", "")

            # Try extracting pieces that appear between object repr boundaries
            # Support several common SDK chunk-type names and common metadata keys
            sdk_names = r"ChatCompletionChunk|StreamingTextResponse|TextIteratorStreamer|ChatCompletionResponse"
            meta_keys = r"finish_reason|index|created|model|object|service_tier|usage|obfuscation"
            parts = re.findall(r"\)\s*([\s\S]*?)(?=(?:" + sdk_names + r"|,\s*(?:" + meta_keys + r")|$))", s)
            if parts:
                combined = "".join(p for p in parts)
                if combined:
                    return _clean_text(combined)

            # Fallback: capture trailing text after the last ')' up to end
            m = re.search(r"\)\s*([\s\S]+)$", s)
            if m:
                text = m.group(1)
                if text:
                    return _clean_text(text)

            return s

        # If repr fallback is disabled, return empty string to indicate no content from repr
        return ""
    except Exception:
        return str(chunk)


__all__ = ["get_chunk_content"]
