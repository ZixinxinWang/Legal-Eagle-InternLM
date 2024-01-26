<div align="center">
  
![Image](./img/logo.png)

</div><div align="left">
<h1>Legal-Eagle-InternLM</h1>
</div>

Legal-Eagle-InternLM 是一个基于商汤科技和上海人工智能实验室推出的书生浦语大模型InternLM的法律问答机器人。旨在为用户提供符合3H（即Helpful、Honest、Harmless）原则的专业、智能、全面的**法律服务**的法律领域大模型。(**项目logo由DALL·E生成**)

项目的主要贡献者：

[@JakChen797](https://github.com/JakChen797)、[@ZixinxinWang](https://github.com/ZixinxinWang) 、[@sped-zhang](https://github.com/sped-zhang)

## 📖 Introduction

<p></p>

Legal-Eagle-InternLM是一款智能法律系统，具备出色的法律文本处理、法律推理和知识检索能力，可适用于多种用户和不同场景，具有以下主要特点：

* **法律文本处理：** 我们在理解和生成法律语言方面表现出色，包括信息提取和文本摘要。我们通过微调数据，使用了来自NLP司法任务的公开数据以及真实世界的法律相关文本，以提高这一能力。
* **法律推理能力：** 为了满足智慧司法领域的需求，我们的微调数据集采用了法律三段论这一法理推理理论来设计，从而显著增强了模型的法律推理能力。
* **司法领域知识检索：** 我们为智能法律处理系统添加了检索增强模块，提高了系统对背景知识的检索和遵循能力。

## 😊 Features

本项目基于书生·浦语工具链中InternLM、XTuner、LMDeploy、OpenXLab等链路工具，主要内容有模型的监督微调、检索增强生成、主客观评测与量化部署四个部分：
- **监督微调：** 本项目分别在 **30w条法律问答** [DISC-Law-SFT 数据集](https://huggingface.co/datasets/ShengbinYue/DISC-Law-SFT) 微调了InternLM-chat-7B、InternLM2-chat-7B两款模型，并公布权重。另外在[52k单轮问答和带有法律依据的情景问答92k数据集](https://github.com/LiuHC0428/LAW-GPT) 上微调了InternLM2-chat-20B模型，并公布权重。
- **检索增强：** 我们在Legal-Eagle-InternLM 的基础上增加了一个基于开源检索框架 [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) 的检索模块。我们的知识库目前仅包含法条库，法条库包含 **200 多部** 国家法律、条例和规定，其中包括《宪法》、《宪法相关法》、《民法典》、《民法商法》、《行政法》、《经济法》、《社会法》、《刑法》、《诉讼与非诉讼程序法》。
- **主客观评测：** 
  - **客观评测：** 客观评价数据集由一系列中国法律标准化考试和知识竞赛的单项和多项选择题组成，并根据内容复杂性和演绎难度，将问题分为困难、中等和简单三个层次。它可以提供一个更具挑战性和可靠的方法来衡量模型是否可以利用其知识来推理正确的答案。我们通过一系列正则表达式来匹配模型回复中所选择的选项，并将其与标准答案比对，最终通过计算模型回答争取的题目的百分比来衡量模型的客观题答题性能。
  - **主观评测：** 目前仅支持人工判断。后期计划加入GPT4模型打分的方式。
- **量化部署：** 借助LMDeploy工具进行大模型的量化部署。尤其是InternLM2-chat-20B模型的部署。
  
## 📚 Release Models

| Model                                                                                                       | Base Model                                                                                                     | Introduction                                                                                                                                                                 | 
|:------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Legal-Eagle-InternLM-chat-7B     | InternLM-chat-7B                              | 在30w条法律问答[DISC-Law-SFT 数据集](https://huggingface.co/datasets/ShengbinYue/DISC-Law-SFT) 了一版InternLM-chat-7B模型，法律问答效果有提升，发布微调后的LoRA权重                                 |
| Legal-Eagle-InternLM2-chat-7B     | InternLM2-chat-7B                              | 在30w条法律问答[DISC-Law-SFT 数据集](https://huggingface.co/datasets/ShengbinYue/DISC-Law-SFT) 了一版InternLM2-chat-7B模型，法律问答效果有提升，发布微调后的LoRA权重                                |
| Legal-Eagle-InternLM2-chat-20B     | InternLM2-chat-20B                              | 在[52k单轮问答](https://github.com/LiuHC0428/LAW-GPT)和[带有法律依据的情景问答92k数据集](https://github.com/LiuHC0428/LAW-GPT) 上微调了InternLM2-chat-20B模型，法律问答效果有提升，发布微调后的LoRA权重 |

## 💕 Acknowledgements 

本项目基于如下开源项目展开，在此对相关项目和开发人员表示诚挚的感谢：

- [**DISC-LawLLM**](https://github.com/FudanDISC/DISC-LawLLM)
- [**LLaMA-Factory**](https://github.com/hiyouga/LLaMA-Factory)
- [**MedicalGPT**](https://github.com/shibing624/MedicalGPT)
- [**Langchain-Chatchat**](https://github.com/chatchat-space/Langchain-Chatchat)
- [**xtuner**](https://github.com/InternLM/xtuner)
- [**lmdeploy**](https://github.com/InternLM/lmdeploy)

感谢上海人工智能实验室推出的 **书生·浦语大模型实战营** 提供的技术指导和算力支持，同样感谢其他限于篇幅未能列举的为本项目提供了重要帮助的工作。

## ⚠️ Attention

Legal-Eagle-InternLM 存在一些问题和缺陷，这些问题目前大型语言模型尚未完全解决。尽管该模型在许多任务和情境下能够提供法律相关服务，但需要明确的是，该模型仅供用户参考之用，不能代替专业律师和法律专家的意见和建议。我们鼓励使用 Legal-Eagle-InternLM 的用户以批判性的态度来评估模型的输出，并要理解我们不对因使用该模型而引发的任何问题、风险或不良后果承担责任
