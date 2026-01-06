## Joint Entropy

Let's formalize the setup of the information theory problem before jumping into joint entropy. So far we've been considering three systems:

1) **Encoder** – compresses a source message  
2) **Channel** – a medium used to send information to the decoder  
3) **Decoder** – recovers the original source message from the compressed message sent across the channel  
<div align="center">

<img src="encoder_decode.png" width="290px">
</div>
Let's pause and think about a few channels:

1) A cell phone (source) talking over a channel (air) to a cell phone tower (decoder)  
2) DNA being copied from a source chromosome to a new chromosome (decoder) during mitosis through protein-mediated mechanisms  
3) A user in the past (encoder) storing information on a hard disk (channel) to read it back in the future (decoder)  

So far we've talked about sending one message at a time in isolation, calculating the surprise that an observed event carries. We then computed **entropy** as the expected (weighted) surprise across the entire probability distribution of possible events.

Joint entropy looks at the uncertainty in sending multiple messages together from the sender as a single codeword.  
From the encoder’s view, it asks: if I were to send these two messages together, how efficiently can I compress them into a single message?  

From the decoder’s view, once I see these two events happen together as a single observation, how much does this observation collapse my prior probability distribution?  
These are two perspectives of the same question.

$$
H(X,Y)
= \mathbb{E}_{(x,y)}\!\left[-\log_2 P(x,y)\right]
= - \sum_{x,y} P(x,y)\,\log_2 P(x,y)
$$

Before jumping into the next section, pause and think about this.  Is the joint entropy simply the additive entropy of two events, that is, 
$$
 H(X,Y) = H(X) + H(Y) 
$$

Why or why not?  If we were copying DNA, for example, and saw an A and a C nucleotide appear together, is the surprise of seeing A and C separately equal to the surprise of seeing the combined codeword AC? Why or why not?
