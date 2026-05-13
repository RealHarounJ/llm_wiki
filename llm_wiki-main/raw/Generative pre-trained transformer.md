---
title: "Generative pre-trained transformer"
source: "https://en.wikipedia.org/wiki/Generative_pre-trained_transformer"
author:
  - "[[Wikipedia]]"
published: 2023-02-07
created: 2026-05-05
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Full_GPT_architecture.svg/250px-Full_GPT_architecture.svg.png)

Original GPT model

A **generative pre-trained transformer** (**GPT**) is a type of [large language model](https://en.wikipedia.org/wiki/Large_language_model "Large language model") (LLM) [^1] [^2] [^3] that is widely used in [generative artificial intelligence](https://en.wikipedia.org/wiki/Generative_artificial_intelligence "Generative artificial intelligence") [chatbots](https://en.wikipedia.org/wiki/Chatbot "Chatbot").[^4] [^5] GPTs are based on a [deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning") architecture called the [transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\) "Transformer (deep learning architecture)"). They are pre-trained on large [datasets](https://en.wikipedia.org/wiki/Dataset_\(machine_learning\) "Dataset (machine learning)") of unlabeled content, and able to generate novel content.[^2] [^3]

[OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") was the first to apply generative pre-training to the transformer architecture, introducing the [GPT-1](https://en.wikipedia.org/wiki/GPT-1 "GPT-1") model in 2018.[^6] The company has since released many bigger GPT models. The chatbot [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT"), released in late 2022 (using [GPT-3.5](https://en.wikipedia.org/wiki/GPT-3.5 "GPT-3.5")), was followed by many competitor chatbots using their own generative pre-trained transformers to generate text, such as [Gemini](https://en.wikipedia.org/wiki/Gemini_\(chatbot\) "Gemini (chatbot)"), [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek_\(chatbot\) "DeepSeek (chatbot)") and [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\) "Claude (language model)").

GPTs are primarily used to generate text, but can be trained to generate other kinds of data. For example, [GPT-4o](https://en.wikipedia.org/wiki/GPT-4o "GPT-4o") can process and generate text, images and audio.[^7] To improve performance on complex tasks, some GPTs, such as [OpenAI o3](https://en.wikipedia.org/wiki/OpenAI_o3 "OpenAI o3"), allocate more computation time analyzing the problem before generating an output, and are called [reasoning models](https://en.wikipedia.org/wiki/Reasoning_model "Reasoning model"). In 2025, [GPT-5](https://en.wikipedia.org/wiki/GPT-5 "GPT-5") was released with a router that automatically selects whether to use a faster model or slower reasoning model based on the provided task.

## Background

During the 2010s, improved [machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning") algorithms, more powerful computers, and an increase in the amount of digitized material allowed for an [AI boom](https://en.wikipedia.org/wiki/AI_boom "AI boom").[^8]

Separately, the concept of generative pre-training (GP) was a long-established technique in machine learning. GP is a form of [self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning") wherein a model is first trained on a large, unlabeled dataset (the "pre-training" step) to learn to generate data points. This pre-trained model is then adapted to a specific task using a labeled dataset (the " [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\) "Fine-tuning (deep learning)") " step).[^9]

The transformer architecture for deep learning is the core technology of a GPT. Developed by researchers at [Google](https://en.wikipedia.org/wiki/Google "Google"), it was introduced in the paper " [Attention Is All You Need](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need "Attention Is All You Need") ", which was released on June 12, 2017. The transformer architecture solved many of the performance issues that were associated with older [recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network "Recurrent neural network") (RNN) designs for [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") (NLP). The architecture's use of an [attention mechanism](https://en.wikipedia.org/wiki/Attention_\(machine_learning\) "Attention (machine learning)") allows models to process entire sequences of text at once, enabling the training of much larger and more sophisticated models. Since 2017, available transformer-based NLP systems have been capable of processing, mining, organizing, connecting, contrasting, and [summarizing texts](https://en.wikipedia.org/wiki/Automatic_summarization "Automatic summarization") as well as [answering questions](https://en.wikipedia.org/wiki/Question_answering "Question answering") from textual input.

## History

On June 11, 2018, OpenAI researchers and engineers published a paper called "Improving Language Understanding by Generative Pre-Training", which introduced [GPT-1](https://en.wikipedia.org/wiki/GPT-1 "GPT-1"), the first GPT model.[^10] It was designed as a transformer-based [large language model](https://en.wikipedia.org/wiki/Large_language_model "Large language model") that used generative pre-training (GP) on [BookCorpus](https://en.wikipedia.org/wiki/BookCorpus "BookCorpus"), a diverse [text corpus](https://en.wikipedia.org/wiki/Text_corpus "Text corpus"), followed by discriminative [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(machine_learning\) "Fine-tuning (machine learning)") to focus on specific language tasks.[^11] This semi-supervised approach was seen as a breakthrough. Previously, the best-performing neural models in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") (NLP) had commonly employed [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning") from large amounts of manually labeled data – training a large language model with this approach would have been prohibitively expensive and time-consuming.[^10]

On February 14, 2019, OpenAI introduced [GPT-2](https://en.wikipedia.org/wiki/GPT-2 "GPT-2"), a larger model that could generate coherent text. Created as a direct scale-up of its predecessor, it had both its parameter count and dataset size increased by a factor of 10. GPT-2 has 1.5 billion parameters and was trained on WebText, a 40-gigabyte dataset of 8 million [web pages](https://en.wikipedia.org/wiki/Web_page "Web page").[^12] [^13] Citing risks of malicious use, OpenAI opted for a "staged release", initially publishing smaller versions of the model before releasing the full 1.5-billion-parameter model in November.[^14]

On February 10, 2020, [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft") introduced its Turing Natural Language Generation, which it claimed was the "largest language model ever published at 17 billion parameters." The model outperformed all previous language models at a variety of tasks, including [summarizing texts](https://en.wikipedia.org/wiki/Automatic_summarization "Automatic summarization") and [answering questions](https://en.wikipedia.org/wiki/Question_answering "Question answering").[^15]

On May 28, 2020, OpenAI introduced [GPT-3](https://en.wikipedia.org/wiki/GPT-3 "GPT-3"), a model with 175 billion parameters that was trained on a larger dataset compared to GPT-2. It marked a significant advancement in few-shot and zero-shot learning abilities. With few examples, it could perform various tasks that it was not explicitly trained for.[^16] [^17]

Following the release of GPT-3, OpenAI started using [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback") (RLHF) to align models' behavior more closely with human preferences. This led to the development of [InstructGPT](https://en.wikipedia.org/wiki/InstructGPT "InstructGPT"), a fine-tuned version of GPT-3. OpenAI further refined InstructGPT to create [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT"), the flagship chatbot product of OpenAI that was launched on November 30, 2022.[^18] ChatGPT was initially based on [GPT-3.5](https://en.wikipedia.org/wiki/GPT-3.5 "GPT-3.5"), but it was later transitioned to the [GPT-4](https://en.wikipedia.org/wiki/GPT-4 "GPT-4") model, which was released on March 14, 2023.[^19] [^20] GPT-4 was also integrated into parts of several applications, including [Microsoft Copilot](https://en.wikipedia.org/wiki/Microsoft_Copilot "Microsoft Copilot"), [GitHub Copilot](https://en.wikipedia.org/wiki/GitHub_Copilot "GitHub Copilot"), [Snapchat](https://en.wikipedia.org/wiki/Snapchat "Snapchat"), [Khan Academy](https://en.wikipedia.org/wiki/Khan_Academy "Khan Academy"), and [Duolingo](https://en.wikipedia.org/wiki/Duolingo "Duolingo").[^21]

The immense popularity of ChatGPT spurred widespread development of competing GPT-based systems from other organizations. [EleutherAI](https://en.wikipedia.org/wiki/EleutherAI "EleutherAI") released a series of [open-weight models](https://en.wikipedia.org/wiki/Open-source_artificial_intelligence "Open-source artificial intelligence"), including [GPT-J](https://en.wikipedia.org/wiki/GPT-J "GPT-J") in 2021. Other major technology companies later developed their own GPT models, such as [Google](https://en.wikipedia.org/wiki/Google "Google") 's [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM") and [Gemini](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini (language model)") as well as [Meta AI](https://en.wikipedia.org/wiki/Meta_AI "Meta AI") 's [Llama](https://en.wikipedia.org/wiki/Llama_\(language_model\) "Llama (language model)").[^22]

Many subsequent GPT models have been trained to be [multimodal](https://en.wikipedia.org/wiki/Multimodal_learning "Multimodal learning") (able to process or to generate multiple types of data). For example, [GPT-4o](https://en.wikipedia.org/wiki/GPT-4o "GPT-4o") can both process and generate text, images, and audio.[^23] Additionally, GPT models like [o3](https://en.wikipedia.org/wiki/OpenAI_o3 "OpenAI o3") and [DeepSeek R1](https://en.wikipedia.org/wiki/DeepSeek_R1 "DeepSeek R1") have been trained with [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning") to generate multi-step [chain-of-thought](https://en.wikipedia.org/wiki/Chain_of_thought_prompting "Chain of thought prompting") reasoning before producing a final answer, which helps to solve complex problems in domains such as mathematics.[^24]

On August 7, 2025, OpenAI released [GPT-5](https://en.wikipedia.org/wiki/GPT-5 "GPT-5"), which includes a router that automatically selects whether to use a faster model or slower reasoning model based on task.[^25] [^26]

## Foundation models

A [foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model") is an AI model trained on broad data at scale such that it can be adapted to a wide range of downstream tasks.[^27] [^28]

The most recent [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") 's *GPT-n* series model is [GPT-5](https://en.wikipedia.org/wiki/GPT-5 "GPT-5").[^29]

Other such models include [Google](https://en.wikipedia.org/wiki/Google "Google") 's [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM"), a broad foundation model that has been compared to [GPT-3](https://en.wikipedia.org/wiki/GPT-3 "GPT-3") and has been made available to developers via an [API](https://en.wikipedia.org/wiki/API "API"),[^30] [^31] and Together's GPT-JT, which has been reported as the closest-performing [open-source](https://en.wikipedia.org/wiki/Open-source "Open-source") alternative to [GPT-3](https://en.wikipedia.org/wiki/GPT-3 "GPT-3") (and is derived from [earlier open-source GPTs](https://en.wikipedia.org/wiki/EleutherAI#GPT_models "EleutherAI")).[^32] [Meta AI](https://en.wikipedia.org/wiki/Meta_AI "Meta AI") (formerly [Facebook](https://en.wikipedia.org/wiki/Facebook "Facebook")) also has a generative transformer-based foundational large language model, known as [LLaMA](https://en.wikipedia.org/wiki/LLaMA "LLaMA").[^33]

Foundational GPTs can also employ [modalities](https://en.wikipedia.org/wiki/Modality_\(human%E2%80%93computer_interaction\) "Modality (human–computer interaction)") other than text, for input and/or output. [GPT-4](https://en.wikipedia.org/wiki/GPT-4 "GPT-4") is a multi-modal LLM that is capable of processing text and image input (though its output is limited to text).[^34] Regarding multimodal *output*, some generative transformer-based models are used for [text-to-image](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model") technologies such as [diffusion](https://en.wikipedia.org/wiki/Diffusion_model "Diffusion model") [^35] and parallel decoding.[^36] Such kinds of models can serve as visual foundation models (VFMs) for developing downstream systems that can work with images.[^37]

## Efficient transformer architectures

The computational and memory requirements of [transformer-based models](https://en.wikipedia.org/wiki/Transformer_\(machine_learning_model\) "Transformer (machine learning model)") increase significantly as they scale to larger sizes and longer input sequences. The standard [self-attention](https://en.wikipedia.org/wiki/Attention_\(machine_learning\)#Self-attention "Attention (machine learning)") mechanism has a quadratic complexity with respect to input sequence length, as described in *[Attention Is All You Need](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need "Attention Is All You Need")*. [^38]

Researchers proposed a number of efficiency improvements like sparse attention mechanisms and memory-efficient architectures that reduce computational costs while supporting longer context windows.[^39] Models like BigBird, Reformer, and FlashAttention demonstrate structured attention patterns or optimized computation to improve scalability and efficiency.[^40] [^41] [^42]

This has helped [large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") to efficiently process long input sequences with reduced memory and computation during both training and inference.

## Task-specific models

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Three-stage_large_language_model_training_workflow.svg/500px-Three-stage_large_language_model_training_workflow.svg.png)

Training workflow of original ChatGPT/InstructGPT release 43 44

A foundational GPT model can be further adapted to produce more targeted systems directed to specific tasks and/or subject-matter domains. Methods for such adaptation can include additional [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(machine_learning\) "Fine-tuning (machine learning)") (beyond that done for the foundation model) as well as certain forms of [prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering").[^45]

An important example of this is [fine-tuning models to follow instructions](https://en.wikipedia.org/wiki/Instruction_tuning "Instruction tuning"), which is of course a fairly broad task but more targeted than a foundation model. In January 2022, [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") introduced "InstructGPT" – a series of models which were fine-tuned to follow instructions using a combination of [supervised](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning") training and [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback") (RLHF) on base GPT-3 language models.[^46] [^47] Advantages this had over the bare foundational models included higher accuracy, less negative/toxic sentiment, and generally better alignment with user needs. Hence, OpenAI began using this as the basis for its [API](https://en.wikipedia.org/wiki/API "API") service offerings.[^48] Other instruction-tuned models have been released by others, including a fully open version.[^49] [^50]

Another (related) kind of task-specific models are [chatbots](https://en.wikipedia.org/wiki/Chatbots "Chatbots"), which engage in human-like conversation. In November 2022, OpenAI launched [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT") – an online chat interface powered by an instruction-tuned language model trained in a similar fashion to InstructGPT.[^51] They trained this model using RLHF, with human AI trainers providing conversations in which they played both the user and the AI, and mixed this new dialogue dataset with the InstructGPT dataset for a conversational format suitable for a chatbot. Other major chatbots currently include [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft") 's [Bing Chat](https://en.wikipedia.org/wiki/Bing_Chat "Bing Chat"), which uses OpenAI's [GPT-4](https://en.wikipedia.org/wiki/GPT-4 "GPT-4") (as part of a broader close collaboration between OpenAI and Microsoft),[^52] and [Google](https://en.wikipedia.org/wiki/Google "Google") 's competing chatbot [Gemini](https://en.wikipedia.org/wiki/Gemini_\(chatbot\) "Gemini (chatbot)") (initially based on their [LaMDA](https://en.wikipedia.org/wiki/LaMDA "LaMDA") family of conversation-trained language models, with plans to switch to [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM")).[^53]

Yet another kind of task that a GPT can be used for is the [meta](https://en.wikipedia.org/wiki/Meta_\(prefix\) "Meta (prefix)") -task of generating *its own* instructions, like developing a series of prompts for 'itself' to be able to effectuate a more general goal given by a human user.[^54] This is known as an AI [agent](https://en.wikipedia.org/wiki/Software_agent "Software agent"), and more specifically a recursive one because it uses results from its previous self-instructions to help it form its subsequent prompts; the first major example of this was [Auto-GPT](https://en.wikipedia.org/wiki/Auto-GPT "Auto-GPT") (which uses OpenAI's GPT models), and others have since been developed as well.[^55]

Chain-of-thought reasoning is a prompting technique in which a language model generates intermediate reasoning steps before arriving at a final answer. This approach has been shown to improve performance on tasks requiring multi-step reasoning, such as mathematical problem solving and logical inference.[^56]

By producing step-by-step explanations, the model is able to decompose complex problems into smaller, more manageable parts. This technique is often used in conjunction with few-shot prompting, where examples demonstrating the reasoning process are included in the input.

### Domain-specificity

GPT systems can be directed toward particular fields or domains. Some reported examples of such models and apps are as follows:

- EinsteinGPT – for sales and marketing domains, to aid with customer relationship management (uses [GPT-3.5](https://en.wikipedia.org/wiki/GPT-3.5 "GPT-3.5")) [^57] [^58]
- BloombergGPT – for the financial domain, to aid with financial news and information (uses "freely available" AI methods, combined with their proprietary data) [^59]
- Khanmigo – described as a GPT version for tutoring, in the education domain, it aids students using [Khan Academy](https://en.wikipedia.org/wiki/Khan_Academy "Khan Academy") by guiding them through their studies without directly providing answers (powered by [GPT-4](https://en.wikipedia.org/wiki/GPT-4 "GPT-4")) [^60] [^61]
- SlackGPT – for the [Slack](https://en.wikipedia.org/wiki/Slack_\(software\) "Slack (software)") instant-messaging service, to aid with navigating and summarizing discussions on it (uses [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") 's [API](https://en.wikipedia.org/wiki/API "API")) [^62]
- BioGPT – for the biomedical domain, to aid with biomedical literature text generation and mining (uses [GPT-2](https://en.wikipedia.org/wiki/GPT-2 "GPT-2")) [^63]

Sometimes domain-specificity is accomplished via software [plug-ins or add-ons](https://en.wikipedia.org/wiki/Plug-in_\(computing\) "Plug-in (computing)"). For example, several different companies have developed particular plugins that interact directly with OpenAI's [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT") interface,[^64] [^65] and [Google Workspace](https://en.wikipedia.org/wiki/Google_Workspace "Google Workspace") has available add-ons such as "GPT for Sheets and Docs" – which is reported to aid use of [spreadsheet](https://en.wikipedia.org/wiki/Spreadsheet "Spreadsheet") functionality in [Google Sheets](https://en.wikipedia.org/wiki/Google_Sheets "Google Sheets").[^66] [^67]

## Scaling laws

Scaling laws describe empirical relationships between the performance of large [language models](https://en.wikipedia.org/wiki/Language_model "Language model") and factors such as model size, dataset size, and computational resources. Empirical work has found that performance tends to follow approximate power-law relationships as these factors increase.[^68]

Larger models trained on more data generally achieve lower training loss and better generalization. Later work suggests that performance is not determined by parameter count alone, but by how model size, data, and compute are balanced during training.[^69]

These observations have influenced the development of successive GPT models, particularly in decisions about architecture design, dataset composition, and training strategies.

## Emergent abilities

Emergent abilities refer to capabilities that appear in large language models only when they reach a certain scale and are not present in smaller versions of the same models. These abilities are considered "emergent" because they arise as model size, training data, and compute increase.[^70] [^71]

Examples of emergent abilities include multi-step reasoning, in-context learning (the ability to perform tasks based on examples provided in prompts without additional training), and improved performance on complex language and reasoning benchmarks.

Research suggests that these capabilities do not scale linearly, but instead appear once models exceed certain thresholds in size and training scale.[^71]

This phenomenon has influenced the development of larger GPT models and contributed to their increased effectiveness across a wide range of tasks.

## Brand issues

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Smartphone_with_ChatGPT_on_the_US_dollar_banknotes_background_%2852917311070%29.jpg/250px-Smartphone_with_ChatGPT_on_the_US_dollar_banknotes_background_%2852917311070%29.jpg)

OpenAI claims "GPT" to be its own branding, citing its association with ChatGPT and its model versions' designations.

[OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI"), which created the first generative pre-trained transformer (GPT) in 2018, asserted in 2023 that "GPT" should be regarded as a *brand* of OpenAI.[^72] In April 2023, OpenAI revised the brand guidelines in its [terms of service](https://en.wikipedia.org/wiki/Terms_of_service "Terms of service") to indicate that other businesses using its [API](https://en.wikipedia.org/wiki/API "API") to run their AI services would no longer be able to include "GPT" in such names or branding.[^73] In May 2023, OpenAI engaged a brand management service to notify its API customers of this policy, although these notifications stopped short of making overt legal claims (such as allegations of [trademark infringement](https://en.wikipedia.org/wiki/Trademark_infringement "Trademark infringement") or demands to [cease and desist](https://en.wikipedia.org/wiki/Cease_and_desist "Cease and desist")).[^72] As of November 2023, OpenAI still prohibits its API licensees from naming their own products with "GPT",[^74] but it has begun enabling its ChatGPT Plus subscribers to make "custom versions of ChatGPT" called [GPTs](https://en.wikipedia.org/wiki/GPTs "GPTs") on the OpenAI site.[^75] OpenAI's terms of service says that its subscribers may use "GPT" in the names of these, although it's "discouraged".[^74]

Relatedly, OpenAI has applied to the [United States Patent and Trademark Office](https://en.wikipedia.org/wiki/United_States_Patent_and_Trademark_Office "United States Patent and Trademark Office") (USPTO) to seek domestic [trademark registration](https://en.wikipedia.org/wiki/Trademark_registration "Trademark registration") for the term "GPT" in the field of AI.[^72] OpenAI sought to expedite handling of its application, but the USPTO declined that request in April 2023.[^76] In May 2023, the USPTO responded to the application with a determination that "GPT" was both descriptive and generic.[^77] As of November 2023, OpenAI continued to pursue its argument.

For any given type or scope of trademark protection in the U.S., OpenAI would need to establish that the term is actually " [distinctive](https://en.wikipedia.org/wiki/Trademark_distinctiveness "Trademark distinctiveness") " to their specific offerings in addition to being a broader technical term for the kind of technology. Some media reports suggested in 2023 that OpenAI may be able to obtain trademark registration based indirectly on the fame of its GPT-based [chatbot](https://en.wikipedia.org/wiki/Chatbot "Chatbot") product, [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT"),[^76] [^78] for which OpenAI has *separately* sought protection (and which it has sought to enforce more strongly).[^79] Other reports have indicated that registration for the bare term "GPT" seems unlikely to be granted,[^72] [^80] as it is used frequently as a common term to refer simply to AI systems that involve generative pre-trained transformers.[^3] [^81] [^82] [^83] In any event, to whatever extent exclusive rights in the term may occur the U.S., others would need to avoid using it for similar products or services in ways likely to cause confusion.[^80] [^84] If such rights ever became broad enough to implicate other well-established uses in the field, the trademark doctrine of *descriptive fair use* could still continue non-brand-related usage.[^85]

In the [European Union](https://en.wikipedia.org/wiki/European_Union "European Union"), the [European Union Intellectual Property Office](https://en.wikipedia.org/wiki/European_Union_Intellectual_Property_Office "European Union Intellectual Property Office") registered "GPT" as a trade mark of OpenAI in spring 2023. However, since spring 2024 the registration is being challenged and is pending cancellation.[^86]

In [Switzerland](https://en.wikipedia.org/wiki/Switzerland "Switzerland"), the [Swiss Federal Institute of Intellectual Property](https://en.wikipedia.org/wiki/Swiss_Federal_Institute_of_Intellectual_Property "Swiss Federal Institute of Intellectual Property") registered "GPT" as a trade mark of OpenAI in spring 2023.[^87] [^88]

## Evaluation and benchmarking

The evaluation of generative pre-trained transformer models is carried out using a range of benchmarks and metrics, which aim to assess their performance across different tasks. Common approaches include accuracy on standard datasets, as well as other features such as robustness, bias, and toxicity.[^89]

These models are typically tested on tasks such as natural language understanding, reasoning, answering queries, and code generation. Sometimes they combine multiple tasks to provide a broader assessment of model performance across domains.[^90]

More recent approaches extend these evaluations to include other features such as fairness, efficiency, and transparency, in order to get a more accurate assessment of these models.[^89]

Evaluation remains an active area of research, as existing tests may not accurately reflect real-world performance or the risks associated with large-scale generative models.[^89]

## Ethical considerations and societal impact

Generative pre-trained transformer models have raised a range of ethical and societal concerns, particularly regarding bias, misinformation, and environmental impact. Large language models can reproduce and amplify patterns present in their training data, including social biases, which may lead to unfair or misleading outputs.[^91] [^92]

These models have also been associated with generating inaccurate or misleading information, as they are designed to produce fluent text rather than to verify factual accuracy. This has an impact on their use in applications such as automated content generation and information dissemination.[^93]

[^1]: Haddad, Mohammed. ["How does GPT-4 work and how can you start using it in ChatGPT?"](https://www.aljazeera.com/news/2023/3/15/how-do-ai-models-like-gpt-4-work-and-how-can-you-start-using-it). *www.aljazeera.com*. [Archived](https://web.archive.org/web/20230705224641/https://www.aljazeera.com/news/2023/3/15/how-do-ai-models-like-gpt-4-work-and-how-can-you-start-using-it) from the original on July 5, 2023. Retrieved April 10, 2023.

[^2]: ["Generative AI: a game-changer society needs to be ready for"](https://www.weforum.org/agenda/2023/01/davos23-generative-ai-a-game-changer-industries-and-society-code-developers/). *World Economic Forum*. January 9, 2023. [Archived](https://web.archive.org/web/20230425234858/https://www.weforum.org/agenda/2023/01/davos23-generative-ai-a-game-changer-industries-and-society-code-developers/) from the original on April 25, 2023. Retrieved April 8, 2023.

[^3]: ["The A to Z of Artificial Intelligence"](https://time.com/6271657/a-to-z-of-artificial-intelligence/). *Time*. April 13, 2023. [Archived](https://web.archive.org/web/20230616123839/https://time.com/6271657/a-to-z-of-artificial-intelligence/) from the original on June 16, 2023. Retrieved April 14, 2023.

[^4]: Hu, Luhui (November 15, 2022). ["Generative AI and Future"](https://pub.towardsai.net/generative-ai-and-future-c3b1695876f2). *Medium*. [Archived](https://web.archive.org/web/20230605023010/https://pub.towardsai.net/generative-ai-and-future-c3b1695876f2) from the original on June 5, 2023. Retrieved April 29, 2023.

[^5]: ["CSDL | IEEE Computer Society"](https://www.computer.org/csdl/magazine/co/2022/10/09903869/1H0G6xvtREk). *www.computer.org*. [Archived](https://web.archive.org/web/20230428171218/https://www.computer.org/csdl/magazine/co/2022/10/09903869/1H0G6xvtREk) from the original on April 28, 2023. Retrieved April 29, 2023.

[^6]: ["Improving language understanding with unsupervised learning"](https://openai.com/research/language-unsupervised). *openai.com*. June 11, 2018. [Archived](https://web.archive.org/web/20230318210736/https://openai.com/research/language-unsupervised) from the original on March 18, 2023. Retrieved March 18, 2023.

[^7]: Colburn, Thomas. ["OpenAI unveils GPT-4o, a fresh multimodal AI flagship model"](https://www.theregister.com/2024/05/13/openai_gpt4o/). *The Register*. Retrieved May 18, 2024.

[^8]: ["An understanding of AI's limitations is starting to sink in"](https://www.economist.com/technology-quarterly/2020/06/11/an-understanding-of-ais-limitations-is-starting-to-sink-in). *[The Economist](https://en.wikipedia.org/wiki/The_Economist "The Economist")*. June 11, 2020. [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0013-0613](https://search.worldcat.org/issn/0013-0613). [Archived](https://web.archive.org/web/20200731060114/https://www.economist.com/technology-quarterly/2020/06/11/an-understanding-of-ais-limitations-is-starting-to-sink-in) from the original on July 31, 2020. Retrieved July 31, 2020.

[^9]: Erhan, Dumitru; Courville, Aaron; Bengio, Yoshua; Vincent, Pascal (March 31, 2010). ["Why Does Unsupervised Pre-training Help Deep Learning?"](https://proceedings.mlr.press/v9/erhan10a.html). *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics*. JMLR Workshop and Conference Proceedings: 201–208. [Archived](https://web.archive.org/web/20240124195306/https://proceedings.mlr.press/v9/erhan10a.html) from the original on January 24, 2024. Retrieved January 24, 2024.

[^10]: Radford, Alec; Narasimhan, Karthik; Salimans, Tim; Sutskever, Ilya (June 11, 2018). ["Improving Language Understanding by Generative Pre-Training"](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) (PDF). p. 12. [Archived](https://web.archive.org/web/20210126024542/https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) (PDF) from the original on January 26, 2021. Retrieved July 31, 2020.

[^11]: Khandelwal, Umesh (April 1, 2023). ["How Large Language GPT models evolved and work"](https://www.linkedin.com/pulse/how-large-language-gpt-models-evolved-work-umesh-khandelwal). [Archived](https://web.archive.org/web/20230404041003/https://www.linkedin.com/pulse/how-large-language-gpt-models-evolved-work-umesh-khandelwal) from the original on April 4, 2023. Retrieved April 3, 2023.

[^12]: Vincent, James (February 14, 2019). ["OpenAI's new multitalented AI writes, translates, and slanders"](https://www.theverge.com/2019/2/14/18224704/ai-machine-learning-language-models-read-write-openai-gpt2). *[The Verge](https://en.wikipedia.org/wiki/The_Verge "The Verge")*. [Archived](https://web.archive.org/web/20201218091707/https://www.theverge.com/2019/2/14/18224704/ai-machine-learning-language-models-read-write-openai-gpt2) from the original on December 18, 2020. Retrieved December 19, 2020.

[^13]: Radford, Alec; Wu, Jeffrey; Child, Rewon; Luan, David; Amodei, Dario; Sutskever, Ilua (February 14, 2019). ["Language models are unsupervised multitask learners"](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (PDF). *OpenAI*. **1** (8). [Archived](https://web.archive.org/web/20210206183945/https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (PDF) from the original on February 6, 2021. Retrieved December 19, 2020.

[^14]: Vincent, James (November 7, 2019). ["OpenAI has published the text-generating AI it said was too dangerous to share"](https://www.theverge.com/2019/11/7/20953040/openai-text-generation-ai-gpt-2-full-model-release-1-5b-parameters). *The Verge*. [Archived](https://web.archive.org/web/20200611054114/https://www.theverge.com/2019/11/7/20953040/openai-text-generation-ai-gpt-2-full-model-release-1-5b-parameters) from the original on June 11, 2020. Retrieved April 28, 2023.

[^15]: Sterling, Bruce (February 13, 2020). ["Web Semantics: Microsoft Project Turing introduces Turing Natural Language Generation (T-NLG)"](https://www.wired.com/beyond-the-beyond/2020/02/web-semantics-microsoft-project-turing-introduces-turing-natural-language-generation-t-nlg/). *[Wired](https://en.wikipedia.org/wiki/Wired_\(magazine\) "Wired (magazine)")*. [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1059-1028](https://search.worldcat.org/issn/1059-1028). [Archived](https://web.archive.org/web/20201104163637/https://www.wired.com/beyond-the-beyond/2020/02/web-semantics-microsoft-project-turing-introduces-turing-natural-language-generation-t-nlg/) from the original on November 4, 2020. Retrieved July 31, 2020.

[^16]: Sagar, Ram (June 3, 2020). ["OpenAI Releases GPT-3, The Largest Model So Far"](https://analyticsindiamag.com/open-ai-gpt-3-language-model/). *Analytics India Magazine*. [Archived](https://web.archive.org/web/20200804173452/https://analyticsindiamag.com/open-ai-gpt-3-language-model/) from the original on August 4, 2020. Retrieved July 31, 2020.

[^17]: Brown, Tom B.; Mann, Benjamin; Ryder, Nick; Subbiah, Melanie; Kaplan, Jared; Dhariwal, Prafulla; Neelakantan, Arvind; Shyam, Pranav; Sastry, Girish; Askell, Amanda; Agarwal, Sandhini; Herbert-Voss, Ariel; Krueger, Gretchen; Henighan, Tom; Child, Rewon; Ramesh, Aditya; Ziegler, Daniel M.; Wu, Jeffrey; Winter, Clemens; Hesse, Christopher; Chen, Mark; Sigler, Eric; Litwin, Mateusz; Gray, Scott; Chess, Benjamin; Clark, Jack; Berner, Christopher; McCandlish, Sam; Radford, Alec; Sutskever, Ilya; Amodei, Dario (May 28, 2020). "Language Models are Few-Shot Learners". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2005.14165](https://arxiv.org/abs/2005.14165) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].

[^18]: Fu, Yao; Peng, Hao; Khot, Tushar (2022). ["How does GPT Obtain its Ability? Tracing Emergent Abilities of Language Models to their Sources"](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1). *Yao Fu's Notion*. [Archived](https://web.archive.org/web/20230419174208/https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1) from the original on April 19, 2023. Retrieved June 24, 2023.

[^19]: Edwards, Benj (March 14, 2023). ["OpenAI's GPT-4 exhibits "human-level performance" on professional benchmarks"](https://arstechnica.com/information-technology/2023/03/openai-announces-gpt-4-its-next-generation-ai-language-model/). *[Ars Technica](https://en.wikipedia.org/wiki/Ars_Technica "Ars Technica")*. [Archived](https://web.archive.org/web/20230314225236/https://arstechnica.com/information-technology/2023/03/openai-announces-gpt-4-its-next-generation-ai-language-model/) from the original on March 14, 2023. Retrieved March 15, 2023.

[^20]: OpenAI (March 15, 2023). "GPT-4 Technical Report". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2303.08774](https://arxiv.org/abs/2303.08774) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].

[^21]: Gupta, Aman (March 21, 2023). ["GPT-4 takes the world by storm - List of companies that integrated the chatbot"](https://www.livemint.com/technology/tech-news/gpt4-takes-the-world-by-storm-list-of-companies-that-integrated-the-chatbot-11679293885004.html). *[Mint](https://en.wikipedia.org/wiki/Mint_\(newspaper\) "Mint (newspaper)")*. Retrieved January 23, 2024.

[^22]: Alford, Anthony (July 13, 2021). ["EleutherAI Open-Sources Six Billion Parameter GPT-3 Clone GPT-J"](https://www.infoq.com/news/2021/07/eleutherai-gpt-j/). *InfoQ*. [Archived](https://web.archive.org/web/20230210114137/https://www.infoq.com/news/2021/07/eleutherai-gpt-j/) from the original on February 10, 2023. Retrieved April 3, 2023.

[^23]: Colburn, Thomas. ["OpenAI unveils GPT-4o, a fresh multimodal AI flagship model"](https://www.theregister.com/2024/05/13/openai_gpt4o/). *The Register*. Retrieved May 18, 2024.

[^24]: Zia, Dr Tehseen (March 29, 2025). ["How OpenAI's o3, Grok 3, DeepSeek R1, Gemini 2.0, and Claude 3.7 Differ in Their Reasoning Approaches"](https://www.unite.ai/how-openais-o3-grok-3-deepseek-r1-gemini-2-0-and-claude-3-7-differ-in-their-reasoning-approaches/). *Unite.AI*. Retrieved August 3, 2025.

[^25]: Heath, Alex (August 7, 2025). ["GPT-5 is being released to all ChatGPT users"](https://www.theverge.com/openai/748017/gpt-5-chatgpt-openai-release). *[The Verge](https://en.wikipedia.org/wiki/The_Verge "The Verge")*. Retrieved August 7, 2025.

[^26]: ["Introducing GPT‑5"](https://openai.com/index/introducing-gpt-5/). *OpenAI*. August 7, 2025. Retrieved August 7, 2025.

[^27]: ["Introducing the Center for Research on Foundation Models (CRFM)"](https://hai.stanford.edu/news/introducing-center-research-foundation-models-crfm). *Stanford HAI*. August 18, 2021. [Archived](https://web.archive.org/web/20230604175717/https://hai.stanford.edu/news/introducing-center-research-foundation-models-crfm) from the original on June 4, 2023. Retrieved April 26, 2023.

[^28]: ["Reflections on Foundation Models"](https://hai.stanford.edu/news/reflections-foundation-models). *hai.stanford.edu*. October 18, 2021. [Archived](https://web.archive.org/web/20240815084336/https://hai.stanford.edu/news/reflections-foundation-models) from the original on August 15, 2024. Retrieved August 15, 2024.

[^29]: ["Introducing GPT-5"](https://openai.com/index/introducing-gpt-5/). *openai.com*. August 7, 2025. Retrieved August 14, 2025.

[^30]: Vincent, James (March 14, 2023). ["Google opens up its AI language model PaLM to challenge OpenAI and GPT-3"](https://www.theverge.com/2023/3/14/23639313/google-ai-language-model-palm-api-challenge-openai). *The Verge*. [Archived](https://web.archive.org/web/20230314130256/https://www.theverge.com/2023/3/14/23639313/google-ai-language-model-palm-api-challenge-openai) from the original on March 14, 2023. Retrieved April 29, 2023.

[^31]: ["Google Opens Access to PaLM Language Model"](https://aibusiness.com/nlp/google-opens-access-to-palm-language-model). [Archived](https://web.archive.org/web/20230531193140/https://aibusiness.com/nlp/google-opens-access-to-palm-language-model) from the original on May 31, 2023. Retrieved April 29, 2023.

[^32]: Iyer, Aparna (November 30, 2022). ["Meet GPT-JT, the Closest Open Source Alternative to GPT-3"](https://analyticsindiamag.com/meet-gpt-jt-the-closest-open-source-alternative-to-gpt-3/). *Analytics India Magazine*. [Archived](https://web.archive.org/web/20230602011925/https://analyticsindiamag.com/meet-gpt-jt-the-closest-open-source-alternative-to-gpt-3/) from the original on June 2, 2023. Retrieved April 29, 2023.

[^33]: ["Meta Debuts AI Language Model, But It's Only for Researchers"](https://www.pcmag.com/news/meta-debuts-ai-language-model-but-its-only-for-researchers). *PCMAG*. February 24, 2023. [Archived](https://web.archive.org/web/20230719172539/https://www.pcmag.com/news/meta-debuts-ai-language-model-but-its-only-for-researchers) from the original on July 19, 2023. Retrieved May 21, 2023.

[^34]: Islam, Arham (March 27, 2023). ["Multimodal Language Models: The Future of Artificial Intelligence (AI)"](https://web.archive.org/web/20230515010932/https://www.marktechpost.com/2023/03/27/multimodal-language-models-the-future-of-artificial-intelligence-ai/). Archived from [the original](https://www.marktechpost.com/2023/03/27/multimodal-language-models-the-future-of-artificial-intelligence-ai/) on May 15, 2023. Retrieved May 15, 2023.

[^35]: Islam, Arham (November 14, 2022). ["How Do DALL·E 2, Stable Diffusion, and Midjourney Work?"](https://www.marktechpost.com/2022/11/14/how-do-dall%c2%b7e-2-stable-diffusion-and-midjourney-work/). [Archived](https://web.archive.org/web/20230718183647/https://www.marktechpost.com/2022/11/14/how-do-dall%C2%B7e-2-stable-diffusion-and-midjourney-work/) from the original on July 18, 2023. Retrieved May 21, 2023.

[^36]: Saha, Shritama (January 4, 2023). ["Google Launches Muse, A New Text-to-Image Transformer Model"](https://analyticsindiamag.com/google-launches-muse-a-new-text-to-image-transformer-model/). *Analytics India Magazine*. [Archived](https://web.archive.org/web/20230515010939/https://analyticsindiamag.com/google-launches-muse-a-new-text-to-image-transformer-model/) from the original on May 15, 2023. Retrieved May 15, 2023.

[^37]: Wu (et-al), Chenfei (March 8, 2023). "Visual ChatGPT". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2303.04671](https://arxiv.org/abs/2303.04671) \[[cs.CV](https://arxiv.org/archive/cs.CV)\].

[^38]: Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N.; Kaiser, Łukasz; Polosukhin, Illia (2017). ["Attention Is All You Need"](https://papers.neurips.cc/paper/7181-attention-is-all-you-need). *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*.

[^39]: Tay, Yi; Dehghani, Mostafa; Bahri, Dara; Metzler, Donald (2022). "Efficient Transformers: A Survey". *ACM Computing Surveys*. **55** (6): 109:1–109:28. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/3530811](https://doi.org/10.1145%2F3530811).

[^40]: Zaheer, Manzil; Guruganesh, Guru; Dubey, Kumar Avinava; Ainslie, Joshua; Alberti, Chris; Ontañón, Santiago; Pham, Peter; Ravula, Anirudh; Wang, Qifan; Ahmed, Murtaza; Smola, Alexander J. (2020). ["Big Bird: Transformers for Longer Sequences"](https://proceedings.neurips.cc/paper/2020/file/c8512d142a2d849725f31a9a7a361ab9-Paper.pdf) (PDF). *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*.

[^41]: Kitaev, Nikita; Kaiser, Łukasz; Levskaya, Anselm (2020). ["Reformer: The Efficient Transformer"](https://openreview.net/forum?id=rkgNKkHtvB). *International Conference on Learning Representations (ICLR 2020)*.

[^42]: Mittal, Aayush (July 17, 2024). ["Flash Attention: Revolutionizing Transformer Efficiency"](https://www.unite.ai/flash-attention-revolutionizing-transformer-efficiency/). *Unite.AI*. Retrieved November 16, 2024.

[^43]: Ouyang, Long; Wu, Jeff; et al. (March 4, 2022). "Training language models to follow instructions with human feedback". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2203.02155](https://arxiv.org/abs/2203.02155) \[[cs.CL](https://arxiv.org/archive/cs.CL)\].

[^44]: [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") (January 27, 2022). ["Aligning language models to follow instructions"](https://openai.com/index/instruction-following/). *OpenAI*. Retrieved July 29, 2025.

[^45]: Bommasani (et-al), Rishi (July 12, 2022). "On the Opportunities and Risks of Foundation Models". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2108.07258](https://arxiv.org/abs/2108.07258) \[[cs.LG](https://arxiv.org/archive/cs.LG)\].

[^46]: ["Aligning language models to follow instructions"](https://openai.com/research/instruction-following). *openai.com*. [Archived](https://web.archive.org/web/20230323110040/https://openai.com/research/instruction-following) from the original on March 23, 2023. Retrieved March 23, 2023.

[^47]: Ouyang, Long; Wu, Jeff; Jiang, Xu; et al. (November 4, 2022). "Training language models to follow instructions with human feedback". *NeurIPS*. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2203.02155](https://arxiv.org/abs/2203.02155).

[^48]: Ramnani, Meeta (January 28, 2022). ["OpenAI dumps its own GPT-3 for something called InstructGPT, and for right reason"](https://analyticsindiamag.com/openai-dumps-its-own-gpt-3-for-something-called-instructgpt-and-for-right-reason/). *Analytics India Magazine*. [Archived](https://web.archive.org/web/20230604103815/https://analyticsindiamag.com/openai-dumps-its-own-gpt-3-for-something-called-instructgpt-and-for-right-reason/) from the original on June 4, 2023. Retrieved April 29, 2023.

[^49]: ["Stanford CRFM"](https://crfm.stanford.edu/2023/03/13/alpaca.html). *crfm.stanford.edu*. [Archived](https://web.archive.org/web/20230406082332/https://crfm.stanford.edu/2023/03/13/alpaca.html) from the original on April 6, 2023. Retrieved May 15, 2023.

[^50]: ["Free Dolly: Introducing the World's First Truly Open Instruction-Tuned LLM"](https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm). *Databricks*. April 12, 2023. [Archived](https://web.archive.org/web/20230714134230/https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm) from the original on July 14, 2023. Retrieved May 15, 2023.

[^51]: ["Introducing ChatGPT"](https://openai.com/blog/chatgpt). *openai.com*. [Archived](https://web.archive.org/web/20230316001700/https://openai.com/blog/chatgpt/) from the original on March 16, 2023. Retrieved March 16, 2023.

[^52]: Wiggers, Kyle (May 4, 2023). ["Microsoft doubles down on AI with new Bing features"](https://techcrunch.com/2023/05/04/microsoft-doubles-down-on-ai-with-new-bing-features/). [Archived](https://web.archive.org/web/20231207194237/https://techcrunch.com/2023/05/04/microsoft-doubles-down-on-ai-with-new-bing-features/) from the original on December 7, 2023. Retrieved May 4, 2023.

[^53]: ["ChatGPT vs. Bing vs. Google Bard: Which AI Is the Most Helpful?"](https://www.cnet.com/tech/services-and-software/chatgpt-vs-bing-vs-google-bard-which-ai-is-the-most-helpful/). *CNET*. [Archived](https://web.archive.org/web/20230724222201/https://www.cnet.com/tech/services-and-software/chatgpt-vs-bing-vs-google-bard-which-ai-is-the-most-helpful/) from the original on July 24, 2023. Retrieved April 30, 2023.

[^54]: ["Auto-GPT, BabyAGI, and AgentGPT: How to use AI agents"](https://mashable.com/article/autogpt-ai-agents-how-to-get-access). *Mashable*. April 19, 2023. [Archived](https://web.archive.org/web/20230722065813/https://mashable.com/article/autogpt-ai-agents-how-to-get-access) from the original on July 22, 2023. Retrieved May 15, 2023.

[^55]: Marr, Bernard. ["Auto-GPT May Be The Strong AI Tool That Surpasses ChatGPT"](https://www.forbes.com/sites/bernardmarr/2023/04/24/auto-gpt-may-be-the-strong-ai-tool-that-surpasses-chatgpt/). *Forbes*. [Archived](https://web.archive.org/web/20230521205727/https://www.forbes.com/sites/bernardmarr/2023/04/24/auto-gpt-may-be-the-strong-ai-tool-that-surpasses-chatgpt/) from the original on May 21, 2023. Retrieved May 15, 2023.

[^56]: Wei, Jason (2022). ["Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"](https://arxiv.org/abs/2201.11903). *arXiv preprint arXiv:2201.11903*.

[^57]: Morrison, Ryan (March 7, 2023). ["Salesforce launches EinsteinGPT built with OpenAI technology"](https://techmonitor.ai/technology/ai-and-automation/salesforce-einsteingpt-openai-chatgpt). [Archived](https://web.archive.org/web/20230415095633/https://techmonitor.ai/technology/ai-and-automation/salesforce-einsteingpt-openai-chatgpt) from the original on April 15, 2023. Retrieved April 10, 2023.

[^58]: Sharma, Animesh K.; Sharma, Rahul (2023). ["The role of generative pretrained transformers (GPTs) in revolutionising digital marketing: A conceptual model"](https://ideas.repec.org/s/aza/jcms00.html). *Journal of Cultural Marketing Strategy*. **8** (1): 80–90. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.69554/TLVQ2275](https://doi.org/10.69554%2FTLVQ2275).

[^59]: Leswing, Kif (April 13, 2023). ["Bloomberg plans to integrate GPT-style A.I. into its terminal"](https://www.cnbc.com/2023/04/13/bloomberg-plans-to-integrate-gpt-style-ai-into-its-terminal.html). *CNBC*. [Archived](https://web.archive.org/web/20230519205206/https://www.cnbc.com/2023/04/13/bloomberg-plans-to-integrate-gpt-style-ai-into-its-terminal.html) from the original on May 19, 2023. Retrieved May 4, 2023.

[^60]: Melendez, Steven (May 4, 2023). ["Learning nonprofit Khan Academy is piloting a version of GPT called Khanmigo"](https://www.fastcompany.com/90891522/the-learning-nonprofit-khan-academy-piloting-a-version-of-gpt-called-khanmigo). *Fast Company*. [Archived](https://web.archive.org/web/20230511132231/https://www.fastcompany.com/90891522/the-learning-nonprofit-khan-academy-piloting-a-version-of-gpt-called-khanmigo) from the original on May 11, 2023. Retrieved May 22, 2023.

[^61]: ["Khan Academy Pilots GPT-4 Powered Tool Khanmigo for Teachers"](https://thejournal.com/articles/2023/03/14/khan-academy-pilots-gpt-4-powered-tool-khanmigo-for-teachers.aspx). *THE Journal*. [Archived](https://web.archive.org/web/20230507124146/https://thejournal.com/articles/2023/03/14/khan-academy-pilots-gpt-4-powered-tool-khanmigo-for-teachers.aspx) from the original on May 7, 2023. Retrieved May 7, 2023.

[^62]: Hachman, Mark (May 4, 2023). ["Slack GPT will bring AI chatbots to your conversations"](https://www.pcworld.com/article/1807402/slack-gpt-will-bring-ai-chatbots-to-your-conversations.html). *PCWorld*. [Archived](https://web.archive.org/web/20230609193414/https://www.pcworld.com/article/1807402/slack-gpt-will-bring-ai-chatbots-to-your-conversations.html) from the original on June 9, 2023. Retrieved May 4, 2023.

[^63]: Luo (et-al), Renqian (April 3, 2023). "BioGPT: Generative pre-trained transformer for biomedical text generation and mining". *Briefings in Bioinformatics*. **23** (6) bbac409. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2210.10341](https://arxiv.org/abs/2210.10341). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1093/bib/bbac409](https://doi.org/10.1093%2Fbib%2Fbbac409). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID (identifier)") [36156661](https://pubmed.ncbi.nlm.nih.gov/36156661).

[^64]: John, Amy Sarah (May 5, 2023). ["Know about ChatGPT's 13 best plugins, designed to improve your overall user experience"](https://web.archive.org/web/20230509151243/https://wire19.com/chatgpt-plugins/). *Latest Digital Transformation Trends | Cloud News | Wire19*. Archived from [the original](https://wire19.com/chatgpt-plugins/) on May 9, 2023. Retrieved May 7, 2023.

[^65]: ["ChatGPT plugins"](https://openai.com/blog/chatgpt-plugins). *openai.com*. March 13, 2024. [Archived](https://web.archive.org/web/20230323213712/https://openai.com/blog/chatgpt-plugins) from the original on March 23, 2023. Retrieved May 7, 2023.

[^66]: ["How to Use ChatGPT on Google Sheets With GPT for Sheets and Docs"](https://www.makeuseof.com/how-use-chatgpt-google-sheets/). *MUO*. March 12, 2023. [Archived](https://web.archive.org/web/20230619164055/https://www.makeuseof.com/how-use-chatgpt-google-sheets/) from the original on June 19, 2023. Retrieved May 7, 2023.

[^67]: Asay, Matt (February 27, 2023). ["Embrace and extend Excel for AI data prep"](https://www.infoworld.com/article/3689175/embrace-and-extend-excel-for-ai-data-prep.html). *InfoWorld*. [Archived](https://web.archive.org/web/20230602121215/https://www.infoworld.com/article/3689175/embrace-and-extend-excel-for-ai-data-prep.html) from the original on June 2, 2023. Retrieved May 7, 2023.

[^68]: Kaplan, Jared; McCandlish, Sam; Henighan, Tom (2020). ["Scaling Laws for Neural Language Models"](https://arxiv.org/abs/2001.08361). *arXiv preprint arXiv:2001.08361*.

[^69]: Hoffmann, Jordan (2022). ["Training Compute-Optimal Large Language Models"](https://arxiv.org/abs/2203.15556). *arXiv preprint arXiv:2203.15556*.

[^70]: Wei, Jason (2022). ["Emergent Abilities of Large Language Models"](https://arxiv.org/abs/2206.07682). *arXiv preprint arXiv:2206.07682*.

[^71]: Zhao, Wayne Xin (2023). ["A Survey of Large Language Models"](https://arxiv.org/abs/2303.18223). *arXiv preprint arXiv:2303.18223*.

[^72]: Hicks, William (May 10, 2023). ["ChatGPT creator OpenAI is asking startups to remove 'GPT' from their names"](https://www.bizjournals.com/sanfrancisco/inno/stories/news/2023/05/10/openai-startups-gpt.html). *[The Business Journal](https://en.wikipedia.org/wiki/American_City_Business_Journals "American City Business Journals")*. [Archived](https://web.archive.org/web/20230628214533/https://www.bizjournals.com/sanfrancisco/inno/stories/news/2023/05/10/openai-startups-gpt.html) from the original on June 28, 2023. Retrieved May 21, 2023.

[^73]: OpenAI (April 24, 2023). ["Brand Guidelines"](https://openai.com/brand). [Archived](https://web.archive.org/web/20230718140318/https://openai.com/brand) from the original on July 18, 2023. Retrieved May 21, 2023.

[^74]: ["Brand guidelines"](https://openai.com/brand#models). [Archived](https://web.archive.org/web/20230718140318/https://openai.com/brand#models) from the original on July 18, 2023. Retrieved November 28, 2023.

[^75]: ["Introducing GPTS"](https://openai.com/blog/introducing-gpts). March 13, 2024. [Archived](https://web.archive.org/web/20240320152321/https://openai.com/blog/introducing-gpts) from the original on March 20, 2024. Retrieved November 28, 2023.

[^76]: Heah, Alexa (April 26, 2023). ["OpenAI Unsuccessful At Speeding Up Its Attempt To Trademark 'GPT'"](https://designtaxi.com/news/423211/OpenAI-Unsuccessful-At-Speeding-Up-Its-Attempt-To-Trademark-GPT/). *DesignTAXI*. [Archived](https://web.archive.org/web/20230426090310/https://designtaxi.com/news/423211/OpenAI-Unsuccessful-At-Speeding-Up-Its-Attempt-To-Trademark-GPT/) from the original on April 26, 2023. Retrieved May 21, 2023.

[^77]: ["NONFINAL OFFICE ACTION"](https://tsdr.uspto.gov/documentviewer?caseId=sn97733259&docId=NFIN20230525093517#docIndex=4&page=1). *USPTO*. May 25, 2023. [Archived](https://web.archive.org/web/20231203101937/https://tsdr.uspto.gov/documentviewer?caseId=sn97733259&docId=NFIN20230525093517#docIndex=4&page=1) from the original on December 3, 2023. Retrieved December 30, 2023.

[^78]: ["OpenAI Wants to Trademark 'GPT' Amid Rise of AI Chatbots"](https://www.techtimes.com/articles/290766/20230425/openai-trademark-gpt-chatgpt-rise-ai-chatbots.htm). Tech Times. April 25, 2023. [Archived](https://web.archive.org/web/20230425151024/https://www.techtimes.com/articles/290766/20230425/openai-trademark-gpt-chatgpt-rise-ai-chatbots.htm) from the original on April 25, 2023. Retrieved May 21, 2023.

[^79]: Louise, Nickie (April 3, 2023). ["OpenAI files a UDRP case against the current owner of ChatGPT.com"](https://techstartups.com/2023/04/03/openai-files-a-udrp-case-against-the-current-owner-of-chatgpt-com/). [Archived](https://web.archive.org/web/20230605031229/https://techstartups.com/2023/04/03/openai-files-a-udrp-case-against-the-current-owner-of-chatgpt-com/) from the original on June 5, 2023. Retrieved May 21, 2023.

[^80]: Demcak, Tramatm-Igor (April 26, 2023). ["OpenAI's Battle for Brand Protection: Can GPT be trademarked?"](https://web.archive.org/web/20230505162827/https://www.lexology.com/library/detail.aspx?g=763049f7-7ef8-4a68-bdb1-2e4fa194b7ad). *Lexology*. Archived from [the original](https://www.lexology.com/library/detail.aspx?g=763049f7-7ef8-4a68-bdb1-2e4fa194b7ad) on May 5, 2023. Retrieved May 22, 2023.

[^81]: Lawton, George (April 20, 2023). ["ChatGPT vs. GPT: How are they different? | TechTarget"](https://web.archive.org/web/20230509150052/https://www.techtarget.com/searchenterpriseai/feature/ChatGPT-vs-GPT-How-are-they-different). *Enterprise AI*. Archived from [the original](https://www.techtarget.com/searchenterpriseai/feature/ChatGPT-vs-GPT-How-are-they-different) on May 9, 2023. Retrieved May 21, 2023.

[^82]: Robb, Drew (April 12, 2023). ["GPT-4 vs. ChatGPT: AI Chatbot Comparison"](https://www.eweek.com/artificial-intelligence/gpt-4-vs-chatgpt/). *eWEEK*. [Archived](https://web.archive.org/web/20230727102701/https://www.eweek.com/artificial-intelligence/gpt-4-vs-chatgpt/) from the original on July 27, 2023. Retrieved May 21, 2023.

[^83]: Russo, Philip (August 22, 2023). ["The Genesis of Generative AI for Everything Everywhere All at Once in CRE"](https://commercialobserver.com/2023/08/jll-ai-gpt-proptech/). *Commercial Observer*. [Archived](https://web.archive.org/web/20230824103201/https://commercialobserver.com/2023/08/jll-ai-gpt-proptech/) from the original on August 24, 2023.

[^84]: ["Trademark infringement"](https://www.law.cornell.edu/wex/trademark_infringement). [Archived](https://web.archive.org/web/20231130025605/https://www.law.cornell.edu/wex/trademark_infringement) from the original on November 30, 2023. Retrieved November 29, 2023.

[^85]: Rheintgen, Husch Blackwell LLP-Kathleen A. (August 16, 2013). ["Branding 101: trademark descriptive fair use"](https://www.lexology.com/library/detail.aspx?g=4f7fc6dd-1d5f-41a1-beac-2638750faa75). *Lexology*. [Archived](https://web.archive.org/web/20230521234617/https://www.lexology.com/library/detail.aspx?g=4f7fc6dd-1d5f-41a1-beac-2638750faa75) from the original on May 21, 2023. Retrieved May 21, 2023.

[^86]: ["EUIPO - eSearch"](https://euipo.europa.eu/eSearch/#details/trademarks/018836652). *euipo.europa.eu*. Retrieved September 4, 2025.

[^87]: ["IPI Database"](https://www.swissreg.ch/database-client/register/detail/trademark/1207210904). *www.swissreg.ch*. Retrieved September 4, 2025.

[^88]: Vogt, Reto (February 20, 2024). ["OpenAI sichert sich in der Schweiz "GPT" als Markenname"](https://web.archive.org/web/20250321201434/https://www.inside-it.ch/openai-sichert-sich-in-der-schweiz-gpt-als-markenname-20240220). *www.inside-it.ch* (in German). Archived from [the original](https://www.inside-it.ch/openai-sichert-sich-in-der-schweiz-gpt-als-markenname-20240220,%20https://www.inside-it.ch/openai-sichert-sich-in-der-schweiz-gpt-als-markenname-20240220) on March 21, 2025. Retrieved September 4, 2025.

[^89]: ["Holistic Evaluation of Language Models (HELM)"](https://crfm.stanford.edu/2022/11/17/helm.html). *Stanford Center for Research on Foundation Models*. Retrieved March 31, 2026.

[^90]: ["Holistic Evaluation of Language Models (HELM)"](https://crfm.stanford.edu/helm/classic/v0.3.0/). *Stanford Center for Research on Foundation Models*. Retrieved March 31, 2026.

[^91]: Bender, Emily M.; Gebru, Timnit; McMillan-Major, Angelina; Shmitchell, Shmargaret (2021). *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?*. Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21). pp. 610–623. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/3442188.3445922](https://doi.org/10.1145%2F3442188.3445922).

[^92]: Weidinger, Laura; Mellor, John; Rauh, Maribeth (2022). *Taxonomy of Risks posed by Language Models*. 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22). pp. 214–229. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/3531146.3533088](https://doi.org/10.1145%2F3531146.3533088).

[^93]: Pan, Yikang; Pan, Liangming; Chen, Wenhu; Nakov, Preslav; Kan, Min-Yen; Wang, William Yang (2023). *On the Risk of Misinformation Pollution with Large Language Models*. Findings of the Association for Computational Linguistics: EMNLP 2023. pp. 1389–1403. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.18653/v1/2023.findings-emnlp.97](https://doi.org/10.18653%2Fv1%2F2023.findings-emnlp.97).

[^94]: Strubell, Emma; Ganesh, Ananya; McCallum, Andrew (2019). *Energy and Policy Considerations for Deep Learning in NLP*. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. pp. 3645–3650. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1906.02243](https://arxiv.org/abs/1906.02243). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.18653/v1/P19-1355](https://doi.org/10.18653%2Fv1%2FP19-1355).

[^95]: Ren, Shaolei; Tomlinson, Bill; Black, Rebecca W.; Torrance, Andrew W. (2024). "Reconciling the contrasting narratives on the environmental impact of large language models". *Scientific Reports*. **14**: 26310. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1038/s41598-024-76682-6](https://doi.org/10.1038%2Fs41598-024-76682-6).