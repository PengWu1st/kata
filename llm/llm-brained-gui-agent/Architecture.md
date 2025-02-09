# Architecture
```
llm-gui-agent/
├── src/
│   ├── env/  # 操作环境

│   │   ├── platform.py
│   │   ├── perceiver.py 
│   │   └── feedback.py
│   ├── prompts/  # 提示工程
│   │   ├── templates.py
│   │   └── examples.py  
│   ├── model/  # 模型推理
│   │   ├── planner.py
│   │   └── action.py
│   ├── actions/  # 动作执行
│   │   ├── ui_ops.py
│   │   └── api_calls.py
│   └── memory/  # 记忆系统
│       ├── short_term.py
│       └── long_term.py
```
## Operating Environment

### platform

- Mobile Platforms

- Web Platforms

- Computer Platforms

### environment state perception

- GUI Screenshots

- Widget Trees

- UI Element Propeties

- Complementary CV Approaches

### Enviroment Feedback

- Screenshot update

- UI Structure Change

- Function Return Values and Exceptions



## Prompt Engineering

### User Request

### Agent Instruction

### Environment States

### Action Documents

### Demonstrated Examples

### Complementary Information

## Model Inference

### Planning

### Action Inference

### Complementary Outputs

## Actions Execution

### UI Operations

### Native API Calls

### AI Tools

## Memory

### Short-Term Memory

- Action

- Plan

- Execution Results

- Environment State

### Long-Term Memory

- Self experience

- Self guidance

- Extrernal Knowledge

- Task Success Metrics

## Advanced Enhancements

### Computer Vision-Based GUI Parsing

### Multi-Agent Framework

### Self-Reflection

### Self-Evolution

### Reinforcement Learning

### Summary & Takeaways

