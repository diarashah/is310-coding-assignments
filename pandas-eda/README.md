# Exploring and Visualizing Culture

## Ratings vs Ranking in Top Novels

### Datasets

This analysis uses the Goodreads Top 500 Novels dataset from the Responsible Datasets in Context Project.  
The dataset was loaded directly using a remote URL in Pandas.


### Analysis

This notebook explores whether reader ratings influence how novels are ranked.  
It focuses on the relationship between Goodreads average ratings and the Top 500 ranking.

In addition, it looks at how novels are distributed across genres to better understand the structure of the dataset.



### Questions Explored

- Do higher-rated books tend to have better rankings?
- Is there a clear relationship between ratings and ranking?
- How are novels distributed across different genres?



### Conclusion

The analysis shows that there is no strong relationship between Goodreads ratings and ranking position. Highly rated books are not always ranked at the top, and some lower-rated books still appear among the highest-ranked novels.

This suggests that rankings are influenced by factors beyond reader ratings, such as maybe literary reputation or historical significance.
The genre distribution also shows that some categories appear more frequently than others, indicating that the dataset is not evenly balanced across genres. 

Also the presence of missing genre values highlights limitations in the dataset that affect analysis.