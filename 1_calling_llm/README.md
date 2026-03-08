# LLM Calling Guide

This directory contains comprehensive guides and examples for calling Large Language Models (LLMs) through various methods and providers. Whether you want to use cloud-based APIs or run models locally, this collection provides practical implementations and best practices.

## Directory Structure

```
1_calling_llm/
├── text/                          # Text-only LLM interactions
│   ├── multi_provider_guide.ipynb # Unified APIs across providers
│   ├── native_guide.ipynb         # Direct provider SDKs
│   └── supplementary/             # Supporting materials
│       ├── py_library_*.ipynb     # LangChain/LiteLLM examples
│       ├── HF_with_LangChain...md # HF integration comparison
│       ├── README_streaming.md    # Streaming implementation guide
│       └── streaming_utils.py     # Shared streaming utilities
└── audio_picture/                 # Multimodal LLM interactions
    ├── openai/                    # OpenAI multimodal APIs
    │   ├── multimodal_openai.ipynb
    │   └── file_creation_utils.py
    └── open_source/               # Open-source multimodal
        └── multimodal_opensource.ipynb
```

## Cloud Services: Calling LLMs via APIs

### 1. Original Model Creators

Access LLMs directly from the companies that developed them:

#### **OpenAI**
- **Models**: GPT-4, GPT-4o, GPT-3.5 Turbo, DALL·E, TTS
- **APIs**: Chat Completions, Responses API, Assistants, Images, Audio
- **Features**: Function calling, structured outputs, vision, streaming
- **Pricing**: Pay-per-token usage
- **Examples**: `text/native_guide.ipynb`, `audio_picture/openai/`

#### **Anthropic (Claude)**
- **Models**: Claude 3.5 Sonnet, Opus, Haiku
- **APIs**: Messages API with streaming
- **Features**: Long context (200K+ tokens), tool use, vision
- **Pricing**: Pay-per-token with tiered pricing

#### **Google (Gemini)**
- **Models**: Gemini 1.5 Pro/Flash, multimodal variants
- **APIs**: GenerateContent API
- **Features**: Multimodal (text, images, video), function calling
- **Pricing**: Free tier + pay-per-token

#### **xAI (Grok)**
- **Models**: Grok-1, Grok-1.5, Grok-2
- **APIs**: Direct HTTP requests or SDK
- **Features**: Real-time knowledge, humor, tool integration
- **Pricing**: Free tier + premium access

#### **Mistral AI**
- **Models**: Mistral Large, Medium, 7B/8B variants
- **APIs**: Chat completions with streaming
- **Features**: Strong coding capabilities, multilingual
- **Pricing**: Pay-per-token

#### **Cohere**
- **Models**: Command R+, Aya, multilingual models
- **APIs**: Generate API, chat endpoints
- **Features**: Multilingual support, tool calling
- **Pricing**: Pay-per-token

### 2. Hosted Model Aggregators

Cloud platforms that host and provide access to multiple LLM models from various providers through unified APIs:

#### **Together AI**
- **Models**: Open-source models (Llama, Qwen, Mixtral, etc.)
- **APIs**: OpenAI-compatible endpoints
- **Features**: Serverless inference, fine-tuning
- **Pricing**: Pay-per-token

#### **Groq**
- **Models**: Llama, Mixtral, Gemma (optimized for speed)
- **APIs**: OpenAI-compatible with ultra-low latency
- **Features**: Sub-second response times
- **Pricing**: Pay-per-token

#### **Other Hosted Aggregators**
- **Replicate**: Model marketplace with API access
- **Hugging Face Inference API**: Hosted versions of HF models
- **Anthropic on AWS/Azure**: Enterprise deployments

### 3. Library Frameworks

Code libraries that provide unified interfaces across multiple providers:

#### **LiteLLM**
- **Unified API**: Single interface for 100+ providers
- **Model Format**: `provider/model-name` (e.g., `openai/gpt-4o`, `anthropic/claude-3-5-sonnet-20241022`)
- **Features**: Streaming, function calling, cost tracking, load balancing
- **Local Support**: Ollama, Hugging Face models
- **Example**: `text/multi_provider_guide.ipynb`

#### **LangChain**
- **Unified Interface**: Provider-agnostic `invoke()` and `stream()` methods
- **Integrations**: 50+ LLM providers and platforms
- **Features**: Chains, agents, memory, tool calling
- **Local Support**: Ollama, Hugging Face, local transformers
- **Examples**: `text/supplementary/py_library_langchain*.ipynb`

## Local LLM Calling

Run LLMs directly on your hardware without cloud dependencies:

### 1. Hugging Face Transformers

Run open-source models locally using the Transformers library:

#### **Direct Transformers**
- **Models**: Any model from Hugging Face Hub (13M+ models)
- **Features**: Full control over generation parameters, custom tokenizers
- **Requirements**: Sufficient RAM/VRAM for model size
- **Example**: `text/supplementary/py_library_langchain_hf_local.ipynb`

#### **LangChain Integration**
- **Wrapper**: `HuggingFacePipeline` for unified interface
- **Features**: Consistent API with cloud providers
- **Memory Detection**: Automatic model recommendations based on system RAM
- **Example**: `text/supplementary/py_library_langchain_hf_local.ipynb`

#### **LiteLLM Integration**
- **Model Format**: `huggingface/model-name`
- **Features**: Unified API with cloud providers
- **Limitations**: Less control over generation parameters

### 2. Ollama

User-friendly platform for running LLMs locally:

#### **Features**
- **Models**: Curated collection of optimized models
- **APIs**: OpenAI-compatible REST API
- **Performance**: GPU acceleration, model quantization
- **Management**: Easy model downloading and switching

#### **Integration Options**
- **Native API**: Direct HTTP calls to `localhost:11434`
- **LangChain**: `Ollama` class for unified interface
- **LiteLLM**: `ollama/model-name` format
- **OpenAI Client**: Use base_url parameter to redirect to Ollama

## Multimodal Capabilities

Generate and process multiple content types:

### **Text-to-Image**
- **OpenAI**: DALL·E 3/2 via Images API
- **Open Source**: Stable Diffusion models via Hugging Face
- **Example**: `audio_picture/openai/multimodal_openai.ipynb`

### **Text-to-Speech**
- **OpenAI**: TTS API with multiple voices
- **Open Source**: Bark, Tortoise TTS via Hugging Face
- **Example**: `audio_picture/openai/multimodal_openai.ipynb`

### **Vision Models**
- **GPT-4 Vision**: Image understanding and analysis
- **Claude Vision**: Advanced visual reasoning
- **Gemini Pro Vision**: Multimodal understanding

## Streaming Support

Real-time token-by-token response generation:

### **Implementation Methods**
- **Server-Sent Events (SSE)**: Standard for most APIs
- **LangChain Streaming**: Unified `stream()` method across providers
- **Transformers Streaming**: `TextIteratorStreamer` for local models
- **Custom Implementation**: Manual chunk processing

### **Provider Support**
- **Full Streaming**: OpenAI, Anthropic, Google, Mistral, Groq
- **Local Streaming**: Hugging Face Transformers, Ollama
- **Details**: See `text/supplementary/README_streaming.md`

## Choosing the Right Approach

### **For Prototyping**
- **LiteLLM**: Quick switching between providers
- **LangChain**: Building chains and agents
- **Ollama**: Easy local testing

### **For Production**
- **Native SDKs**: Direct provider access, latest features
- **LangChain**: Complex workflows and integrations
- **Local Models**: Privacy, cost control, offline operation

### **For Cost Optimization**
- **Local Models**: Free after initial setup
- **Groq/Together AI**: Cost-effective open models
- **Provider Tiers**: Volume discounts and commitments

### **For Performance**
- **Groq**: Ultra-low latency
- **Local GPU**: No network overhead
- **Streaming**: Real-time user experience

## Setup and Requirements

### **Cloud APIs**
- API keys for each provider
- `python-dotenv` for secure key management
- Provider-specific SDKs (`openai`, `anthropic`, etc.)

### **Local Models**
- Sufficient RAM (8GB+ recommended)
- GPU optional but recommended
- Hugging Face account for large model downloads
- Ollama installed for simplified local deployment

### **Dependencies**
```bash
# Core packages
pip install langchain langchain-openai langchain-anthropic
pip install litellm openai anthropic google-generativeai

# Local models
pip install transformers torch huggingface-hub
pip install ollama langchain-ollama

# Multimodal
pip install pillow requests
```
