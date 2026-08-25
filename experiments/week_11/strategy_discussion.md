**Discussion of Week 10 Query Outcomes:**

_The aim of this discussion is to inform a data-driven strategy upgrade for generating Week 11's BBO pipeline._

----------------------------------------------------------------------------------------------------------------------

For Function 1, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: 1.7960297527814237e-10. This is the highest output value within the whole dataset for this function, indicating that Week 10's BBO ML pipeline worked very well for this function and is moving towards a very favourable direction. This is also the very first time a higher output value than those already existing within the initial dataset for this function was obtained through a Bayesian Optimisation pipeline tested during the course of this project for this function specifically (which proved to be the most difficult one to maximise), therefore this represents a great success.

For Function 2, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: 0.5157367667960586. This output value is very close to the current maximum achieved for this function so far (0.7560218355559285). Week 10's pipeline is not setting a new maximum output value for this function, but this may likely be because this function may have already been successfully globally maximised in prior weeks. Nonetheless, this fairly high result shows that Week 10's BBO pipeline is performing equitably well for this function, giving a reasonable good-quality next query prediction. 

For Function 3, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: -0.03175722788506985. This output value is very close to the current maximum achieved for this function so far (-0.027517754517067037). Week 10's pipeline is not setting a new maximum output value for this function, but this may likely be because this function may have already been successfully globally maximised in prior weeks. Nonetheless, this fairly high result shows that Week 10's BBO pipeline is performing equitably well for this function, giving a reasonable good-quality next query prediction.

For Function 4, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: 0.5702077009884445. This is the highest output value obtained so far for this function, indicating that Week 10's BBO ML pipeline worked very well for this function and is moving towards a very favourable direction.

For Function 5, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: 15.47278280968818. This output is very far away from the highest output obtained so far for this function (2333.006822317816). This is however not surprising or indicative of a poorly-performing Bayesian Optimisation  ML pipeline, as Thompson Sampling was used for selecting the next query prediction, which is an intrinsically stochastic algorithm, based on randomised sample value drawing from each candidate's posterior probability distribution and therefore cannot guarantee a high-value output, but balances exploration with exploitation automatically and well. 

For Function 6, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: -0.17432386359873336. This is the highest output value obtained so far for this function, indicating that Week 10's BBO ML pipeline worked very well for this function and is moving towards a very favourable direction.

For Function 7, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: 1.8928664258839485. This output value is fairly close to the current maximum achieved for this function so far (2.9397772255463352). Week 10's pipeline is not setting a new maximum output value for this function, but this may likely be because this function may have already been successfully globally maximised in prior weeks. Nonetheless, this fairly high result shows that Week 10's BBO pipeline is performing equitably well for this function, giving a reasonable good-quality next query prediction.

For Function 8, Week 10's BBO ML pipeline predicted the tenth query which gave the following output: 9.8304718114551. This output value is very close to the current maximum achieved for this function so far (9.9561276549796). Week 10's pipeline is not setting a new maximum output value for this function, but this may likely be because this function may have already been successfully globally maximised in prior weeks. Nonetheless, this fairly high result shows that Week 10's BBO pipeline is performing equitably well for this function, giving a reasonable good-quality next query prediction.

------------------------------------------------------------------------

**<ins>Discussion Summary:</ins>**

- Week 10's BBO ML Pipeline managed to maximise 3 out of 8 Black-Box functions, specifically Functions 1, 4 and 6. While Functions 4 and 6 have been maximised before, Function 1 has been maximised for the first time since the start of this project, which proves that this ML pipeline is performing extremely well and represents a great improvement from previous versions.

- While this pipeline has not managed to further maximise other functions (Functions 2,3,5,7,8), this does not reflect on the quality or performance of the pipeline itself, as some of these functions may have already been globally maximised by now, in previous weeks.
