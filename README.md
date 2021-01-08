Answer to “Meaning of Life” by RNN Language Model
Machida Hiroaki

See /5.project-presentation/CS644_Machida-Hiroaki_Presentation.pptx


# How to get started
## Generate a text
python generate_better_text.py

## Train the model (takes 35 hours)
python train_better_rnnlm.py


# Source code
.  
├── generate_better_text.py: generate text  
├── train_better_rnnlm.py: train model  
├── rnnlm_gen.py: generate text class  
├── better_rnnlm.py: RNNLM class  
├── dataset  
│   └── ptb.py: load corpus data  
└── lib  
    ├── time_layers.py: layers for RNNLM  
    ├── trainer.py: train RNNLM  
    ├── optimizer.py: update weights  
    ├── config.py: configure GPU usage  
    ├── util.py: util class  
    ├── np.py: GPU adaptor class  
    └── functions.py  

# Reference
https://github.com/oreilly-japan/deep-learning-from-scratch-2
