Question Answering Module
===================

QA Module (QAM) is divided in two major parts -
- Speech / Textual
- Visual

Visual
-------------
Two layers in the order of increasing priority.
```
1. Person Identification and Gender Recognition.
```
**Example** - Who is the person standing infront? State the gender.
```
2. Basic QA and Object Recognition.
```
**Example** - How many persons are standing infront? Rotate your head towards the person standing on your left. Identify the image, Can you locate a hand/pen/other_object in your frame of reference?

Speech
-----------
Three layers in the order of increasing priority.
```
1. Variable Dynamic Memory Network / RNN/LSTM based Model.
```
In this, we will provide a number of sentences (paragraph) as input to QAM. No boundaries on the state of content.
Refer to [this](http://ethancaballero.pythonanywhere.com/) for reference. The code is in Theano. I am trying to write this on Tensorflow.
```
2. Fixed Dynamic Memory Network / RNN/LSTM based Model.
```
Similar to the previous Network, the input shall be fixed and will contain the Biography of system. The name, who created whom, where are we, what languages do we speak and all related questions can be answered via this layer.

```
3. Basic QA
```
Not exactly QA but this layer shall assist **layer 2** in providing information. More on this later.

**Note** - Majority of the task will be on **Layers 2 and 3** of Speech Module and **entire Visual Module**. 
