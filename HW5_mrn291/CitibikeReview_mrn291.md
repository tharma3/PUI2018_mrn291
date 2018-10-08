# Citibike Review - Martha Norrick mrn291

### Verify that their null and alternative hypotheses are formulated correctly.

The question posed was whether or not Citibike riders under 40 years of age take longer trips on average than riders over 40 years of age.

The null and alternative hypotheses are formulated correctly, 

### Verify that the data supports the project: i.e. if the data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet).

The variables used support the project--they are trip duration (numerical, continuous) and age (numerical, discrete, but in this case used as a category).  The data was preprocessed correctly to produce age from birth year.  Pranay chose to drop instances where birth year was missing from the data and explicitly stated that in the notebook.

### Choose an appropriate test to test H0 given the type of data, and the question asked.

For this question, a comparison of means of two unpaired groups (riders under 40 and riders over 40) where one variable is numerical (trip duration) and the other categorial (over or under 40) I think the most appropriate test is the z-test for unpaired data.  I chose this test because the question is formulated to discover if the samples come from the same population, there are exactly two groups and there are more than 30 observations in each group.  In this case, I think it doesn't matter whether or not the data are parametric or non-parametric since there are enough observations but if the data were smaller the shape of the data would be more important.

Another formulation of this question that might be interesting would be to ask if there is a relationship between age and the length of trip, treating both variables as discrete numberical variables and then testing the correlation between the two of them instead of picking an arbitrary "old age" (which some of us are very close to, just saying) to create a categorial variable.

