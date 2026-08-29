**Discussion of Week 11 Query Outcomes:**

_The aim of this discussion is to inform a data-driven strategy for BBO Week 12._

----------------------------------------------------------------------------------------------------------------------

For Function 1, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: 3.836828661579004e-17. This output value is not very far from the current maximum achieved for this function so far (1.7960297527814237e-10). While Week 11's pipeline is not setting a new maximum output value for this function, this fairly high (for this function) result obtained shows that Week 11's BBO pipeline is performing equitably well for this function, predicting a reasonable good-quality next query point.

For Function 2, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: 0.654999069264761. This is fairly close to the current maximum within the dataset for this function (0.7560218355559285). While Week 11's pipeline is not setting a new maximum output value for this function, this fairly high result obtained shows that Week 11's BBO pipeline is performing equitably well for this function, predicting a reasonable good-quality next query point.

For Function 3, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: -0.01907237834718998. This is the highest output value obtained so far for this function, indicating that Week 11's BBO ML pipeline worked very well for this function.

For Function 4, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: 0.06888650585459688. This is not very close to the current maximum within the dataset for this function (0.5702077009884445), but it still represents a good-quality query prediction, as the dataset for Function 4 contains negative outputs as low as -32.625660215962455. While Week 11's pipeline is not setting a new maximum output value for this function, this obtained result shows that Week 11's BBO pipeline is performing reasonably well.

For Function 5, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: 2215.3917998453526. This is close to the current maximum within the dataset for this function (2333.006822317816). While Week 11 is not setting a new maximum output value for this function (which may likely be because this function may have already been successfully globally maximised), the fairly high result obtained shows that Week 11's BBO pipeline is performing equitably well for this function, predicting a reasonable good-quality next query point. 

For Function 6, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: -0.3364660353920071. This output value is not very far from the current maximum achieved for this function so far (-0.17432386359873336). While Week 11's pipeline is not setting a new maximum output value for this function, this fairly high result obtained shows that Week 11's BBO pipeline is performing equitably well for this function, predicting a reasonable good-quality next query point.

For Function 7, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: 2.7354324994784918. This output value is very close to the current maximum achieved for this function so far (2.9397772255463352). While Week 11's pipeline is not setting a new maximum output value for this function, this fairly high result obtained shows that Week 11's BBO pipeline is performing equitably well for this function, predicting a reasonable good-quality next query point.

For Function 8, Week 11's BBO ML pipeline predicted the eleventh input query which gave the following output: 9.9518480530594. This output value is extremely close to the current maximum achieved for this function so far (9.9561276549796). While Week 11's pipeline is not setting a new maximum output value for this function, this fairly high result obtained shows that Week 11's BBO pipeline is performing equitably well for this function, predicting a reasonable good-quality next query point.

------------------------------------------------------------------------

**<ins>Discussion Summary:</ins>**

At this advanced stage in the BBO capstone project, Week 11's BBO ML Pipeline managed to further maximise 1 out of 8 Black-Box functions, specifically Function 3. Not further maximising the rest of the functions does not reflect on the quality or performance of the pipeline itself, as some (if not many) of these Black-Box functions may have already been globally maximised by now, in previous weeks. In that case, there would be no better points left to be identified through Bayesian Optimisation for those functions and therefore future next query predictions will not be able to override the current already established (global) maxima, regardless of how rigorous and effective the pipeline has become.

As the current Week 11 BBO pipeline is very robust, it will be deployed to predict the next queries for all Black-Box functions during Week 12 (penultimate week) of the BBO project.
