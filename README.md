# LLM Guides

This repository contains comprehensive guides and examples for working with Large Language Models (LLMs), covering setup, calling, prompting, capabilities, agents, Hugging Face integrations, evaluation, and MLOps.

This project is still very much in-progress with a lot of planned files yet to be created. 


## Project Structure

```
pyproject.toml
0_setup/
	detect_local_models.ipynb
	python_environment.md
	computer_model_selection/
		get_specs.ps1
		standardising_comparison.md
		timed_reponses_local_llm.ipynb
		my_computers/
			comparision.md
			computer_1_Mikael_old.md
			computer_2_Terese_DELL.md
			computer_specs_Mikael_Old.txt
			computer3_Mikael.md
1_calling_llm/
	README.md
	audio_picture/
		open_source/
			file_creation_utils.py
			multimodal_opensource.ipynb
			tmp.md
			output/
		openai/
			file_creation_utils.py
			multimodal_openai.ipynb
			output/
	text/
		multi_provider_guide.ipynb
		native_guide.ipynb
		supplementary/
			HF_with_LangChain_or_LiteLLM.md
			py_library_langchain_hf_hosted.ipynb
			py_library_langchain_hf_local.ipynb
			py_library_langchain.ipynb
			py_library_litellm.ipynb
			py_library_openai.ipynb
			README_streaming.md
			streaming_utils.py
			__pycache__/
2_prompting/
3_capabilities/
	data_gathering/
	memory/
		combined_litellm_langchain.ipynb
		langchain.ipynb
		litellm.ipynb
		memory.md
	tool_calling/
4_agents/
	agents_from_scratch/
	agents_readymade/
5_hugging_face/
	README.md
	1_training_finetuning/
		01_accelerate_training.ipynb
		02_fine_tuning_with_transformers.ipynb
		03_peft_fine_tuning.ipynb
		04_datasets_usage.ipynb
		05_tokenizers_usage.ipynb
		06_model_optimization.ipynb
		07_hyperparameter_tuning.ipynb
	2_research/
		01_model_exploration_comparison.ipynb
		02_direct_huggingface_research.ipynb
		03_hugging_face.ipynb
		04_pipelines_vs_nlp.ipynb
		research_guide.md
	3_early_production/
		01_langchain_huggingface_production.ipynb
	4_mature_production/
		01_vllm_tgi_production.ipynb
		02_intro_vllm.ipynb
		03_streaming_vllm.ipynb
		04_serving_api_vllm.ipynb
		05_comparison_ollama.ipynb
		06_gradio_demo.ipynb
		07_langchain_chain.ipynb
6_eval/
7_MLOps/
```