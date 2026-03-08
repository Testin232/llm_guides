# HuggingFace Learning Path: Phase-Based Examples

This directory contains comprehensive examples for integrating HuggingFace models into your applications, organized by development phase. Each phase builds on the previous one, providing the right approach for your current needs.

## 📚 Learning Path Overview

###  Training & Fine-tuning (`1_training_finetuning/`)
**Focus**: Model customization and training techniques
- Basic fine-tuning fundamentals
- Parameter-efficient fine-tuning (PEFT, LoRA)
- Distributed training with Accelerate
- Model optimization and quantization
- Hyperparameter tuning (grid search, Bayesian optimization)
- Dataset preparation and tokenization

**When to use**: When you need to adapt models to your specific tasks
**Key notebook**: `02_fine_tuning_with_transformers.ipynb`

### �🎯 Research Phase (`2_research/`)
**Focus**: Maximum control and experimentation
- Direct transformers usage
- Model inspection and analysis
- Custom generation parameters
- Performance benchmarking
- Research best practices

**When to use**: Learning, prototyping, research projects
**Key notebook**: `02_direct_huggingface_research.ipynb`

### 🏗️ Early Production Phase (`3_early_production/`)
**Focus**: Structured applications with reliability
- LangChain integration
- Error handling and retries
- Conversation memory
- Monitoring and logging
- Production patterns

**When to use**: First production applications, structured workflows
**Key notebook**: `langchain_huggingface_production.ipynb`

### 🏆 Mature Production Phase (`4_mature_production/`)
**Focus**: High-performance serving at scale
- vLLM/TGI optimization
- Async processing and concurrency
- FastAPI server integration
- Comprehensive monitoring
- Enterprise-grade reliability

**When to use**: High-throughput applications, enterprise deployments
**Key notebook**: `01_vllm_tgi_production.ipynb`

## 🚀 Quick Start

### Prerequisites
```bash
pip install transformers torch langchain langchain-huggingface
# For training & fine-tuning
pip install datasets accelerate peft
# For early production
pip install langchain langchain-huggingface
# For mature production
pip install vllm fastapi uvicorn
```

### Choose Your Phase

1. **New to HuggingFace?** → Start with Research Phase
2. **Need to train/fine-tune models?** → Training & Fine-tuning section
3. **Building your first LLM app?** → Early Production Phase
4. **Scaling to thousands of users?** → Mature Production Phase

## 📖 Detailed Guides

### Research Phase: Direct Transformers
- Model loading and configuration
- Custom generation parameters
- Attention analysis and visualization
- Performance benchmarking
- Memory and compute optimization
- Research workflow patterns

### Early Production: LangChain Integration
- Structured prompt templates
- Chain composition and workflows
- Conversation memory management
- Error handling and retries
- Multi-model fallback strategies
- Logging and monitoring setup

### Mature Production: High-Performance Serving
- vLLM/TGI setup and optimization
- Async processing and concurrency
- FastAPI server implementation
- Production monitoring and metrics
- Scaling strategies and load balancing
- Enterprise security and reliability

## 🤔 When to Use LangChain vs. Direct HuggingFace

### Decision Guide

| Use Case | LangChain | LiteLLM | Direct HF |
|----------|-----------|---------|-----------|
| **Simple chat app** | ❌ Overkill | ✅ Good | ✅ Best performance |
| **RAG system** | ✅ Excellent | ⚠️ Limited | 🔧 Manual |
| **Multi-provider app** | ✅ Unified | ✅ Unified | 🔧 Manual switching |
| **Research** | ⚠️ Adds overhead | ❌ Limited | ✅ Full control |

### Key Insights
- **LangChain + HF**: Best for production apps with complex workflows, chains, and multi-provider support.
- **Direct HF**: Ideal for research needing full control and performance.
- **LiteLLM + HF**: Simple unified API for basic multi-provider needs.

### Production Readiness
**LangChain provides:** Structured workflows, error handling, logging, modular architecture.

**Still needed for production:** Model serving (vLLM/TGI), scaling (Kubernetes), optimizations (quantization), monitoring (Prometheus).

## 📈 Progression Path

```
Research Phase (02_direct_huggingface_research.ipynb)
    ↓
Early Production Phase (01_langchain_huggingface_production.ipynb)
    ↓
Mature Production Phase (01_vllm_tgi_production.ipynb)
```

Each phase builds on concepts from the previous, but you can jump in at any level based on your needs.

## 🔧 Additional Resources

### Model Optimization
- Quantization techniques (8-bit, 4-bit)
- GPU memory optimization

### Deployment Options
- Docker containerization
- Kubernetes orchestration
- Cloud deployment (AWS SageMaker, GCP Vertex AI)

### Monitoring & Observability
- Prometheus metrics
- Grafana dashboards
- Distributed tracing

## 🤝 Contributing

Found an issue or want to add an example? Check the main repository for contribution guidelines.

## 📄 License

These examples are provided as educational content for the LLM Engineering course.</content>
<parameter name="filePath">d:/udemy/llm_eng/w-terese/week/2/guides/calling_llm/examples_with_hf/README.md