Recommended Reading and Getting started 
***************************************

.. figure:: https://i.imgur.com/eBRPvWB.png
   :alt: Practical Pytorch

   Practical Pytorch

Recommended Reading
-------------------

I assume you have at least installed PyTorch, know Python, and
understand Tensors:

-  http://pytorch.org/ For installation instructions
-  `Deep Learning with PyTorch: A 60-minute
   Blitz <https://github.com/pytorch/tutorials/blob/master/Deep%20Learning%20with%20PyTorch.ipynb>`__
   to get started with PyTorch in general
-  `jcjohnson's PyTorch
   examples <https://github.com/jcjohnson/pytorch-examples>`__ for a
   wide and deep overview
-  `Introduction to PyTorch for former
   Torchies <https://github.com/pytorch/tutorials/blob/master/Introduction%20to%20PyTorch%20for%20former%20Torchies.ipynb>`__
   if you are a former Lua Torch user

You should know about Recurrent Neural Networks and how they work:

-  `The Unreasonable Effectiveness of Recurrent Neural
   Networks <http://karpathy.github.io/2015/05/21/rnn-effectiveness/>`__
   shows a bunch of real life examples
-  `Deep Learning, NLP, and
   Representations <http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/>`__
   for an overview on word embeddings and RNNs for NLP
-  `Understanding LSTM
   Networks <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>`__
   is about LSTMs specifically but also informative about RNNs in
   general

And for more, read the papers that introduced these topics:

-  `Learning Phrase Representations using RNN Encoder-Decoder for
   Statistical Machine Translation <http://arxiv.org/abs/1406.1078>`__
-  `Sequence to Sequence Learning with Neural
   Networks <http://arxiv.org/abs/1409.3215>`__
-  `Neural Machine Translation by Jointly Learning to Align and
   Translate <https://arxiv.org/abs/1409.0473>`__
-  `A Neural Conversational Model <http://arxiv.org/abs/1506.05869>`__

Get Started
-----------

The quickest way to run these on a fresh Linux or Mac machine is to
install `Anaconda <https://www.continuum.io/anaconda-overview>`__:

::

    curl -LO https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh
    bash Anaconda3-4.3.0-Linux-x86_64.sh

Then install PyTorch:

::

    conda install pytorch -c soumith

Then clone this repo and start Jupyter Notebook:

::

    git clone http://github.com/spro/practical-pytorch
    cd practical-pytorch
    jupyter notebook

Feedback
--------

If you have ideas or find mistakes `please leave a
note <https://github.com/spro/practical-pytorch/issues/new>`__.
