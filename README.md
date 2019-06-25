# Quote-Generation

A Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. 

### Libraries requred
<ul>
  <li>beautiful soup(for web scraping)</li>
  <li>numpy</li>
</ul>

## Working

1. Scrape the data from the internet
2. We create a frequency table in which each key contains k characters and it's corresponding value being the next character that is encountered
3. Obtain the probability for each possible character, given the key value.
4. Sample the next character randomly depending on the probability
