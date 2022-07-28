---
title: An Algorithm For Predicting Australian Elections
output: pdf_document
---
# 1. Introduction

The 2022 Australian Election demonstrated fundamental differences
between first past the post systems and preferential voting systems.
Moreover, the large votes for independents and third parties made the
distribution of preferences critical in determining the composition of
Parliament and the subsequent election of Labor to government. The rise
of the Greens in Brisbane was not predicted, nor expected by traditional
forecasts and independents did far better than many forecasts expected.
While some of this can be attributed to polling error, a deeper problem
about TPP and the method of forecasting elections was exposed. I propose
a new Monte-Carlo method to predict preference flows from previous
elections that better captures the important differences between the
Australian election system and comparative first-past-the-post or
proportional representation systems.

<div style="page-break-after: always;"></div>

# 2. Table Of Contents
- [1. Introduction](#1-introduction)
- [2. Table Of Contents](#2-table-of-contents)
- [3. Outline of Australian Preferential Voting](#3-outline-of-australian-preferential-voting)
  - [3.1. Process](#31-process)
  - [3.2. Counting](#32-counting)
  - [3.3. Two Candidate Preferred](#33-two-candidate-preferred)
  - [3.4. Two Party Preferred](#34-two-party-preferred)
    - [3.4.1. Usefulness of TPP](#341-usefulness-of-tpp)
    - [3.4.2. TPP in 2022 Election](#342-tpp-in-2022-election)
- [4. Forecasting The Australian Election](#4-forecasting-the-australian-election)
  - [4.1. Model Outline](#41-model-outline)
- [5. Predicting National Values](#5-predicting-national-values)
  - [5.1. Fundamentals](#51-fundamentals)
  - [5.2. Polling Data](#52-polling-data)
- [6. Testing seats](#6-testing-seats)
- [7. Predicting Winner From Seat Data](#7-predicting-winner-from-seat-data)
  - [7.1. Polling Data](#71-polling-data)
- [8. Testing seats](#8-testing-seats)
- [9. Predicting Winner From Seat Data](#9-predicting-winner-from-seat-data)

<div style="page-break-after: always;"></div>

# 3. Outline of Australian Preferential Voting

## 3.1. Process

In Australia, the House of Representatives which determines the
government is elected using preferential voting, also known as ranked
choice voting. In the 2022 election, there were 151 division, which each
elected a single member to represent them in the House. In each
division, voters are given a ballot which contains all of the candidates
standing in the election to be a member of that division. Voters than
rank their preferences of who they would prefer to have elected. The
first choice receives a $1$ there second choice a $2$ and so on until
*all* the candidates have been exhausted.[^1] In principle, to determine
who is elected the Australian Electoral Commission performs the
following process

1.  Count all of the first preferences of each of the candidates.

2.  If no one has 50% of the preferences, the lowest candidates is
    eliminated.

3.  The voters who's first preference was eliminated then have their
    second preferences distributed among the remaining candidates.

4.  The process of elimination and distribution of preferences is
    continued until one candidate has greater than 50% of the vote.

5.  The person with greater than 50% of the vote after some number of
    eliminations is then elected.

## 3.2. Counting

The nature of eliminating the lowest ranked candidate and distributing
all their preferences requires that first preference count be absolutely
complete before the elimination is complete. This takes time, not least
because postal can arrive after election (so long as they were posted in
time) and because processes to ensure the correct entry of preferences
take time. The AEC perform preference distributions by entering the
ballot results into a database a computer programme performs the
preference flows. This process takes many days and voters and the media
want indictive results on election night or as soon as possible.

## 3.3. Two Candidate Preferred

Therefore, in practice, the AEC performs a preliminary count at voting
booths on election night. Booth volunteers perform two counts. One count
is of the candidates primary (first preference) vote, the other count is
the two candidate preferred. The two candidate preferred count is
special. The AEC prior to counting nominate two candidates that they
estimate will most likely be the final two after all the elimination
processes are complete. A count is then performed between these two
candidates. A vote for candidate $A$ occurs when a voters has a lower
preference number for $A$ then for $B$.

## 3.4. Two Party Preferred

For much of Australian history election have been contested between the
Liberal/National Coalition (LNP/Liberals) and the Australian Labor Party
(LAB/Labor). The two party system meant that often almost all the seats
in the house were occupied by members of the two **major** parties, with
only a handful of independents and rarely any third parties, until the
2022 election. Because almost all contests in each division have
historically been between the Liberals and Labor it has historically
made sense to refer to contests where the TCP is between a Labor
candidate and a Liberal candidate as a measurement of the two parties'
preferred preferences (TPP).

### 3.4.1. Usefulness of TPP

TPP has been a very useful shorthand for measuring the major parties'
respective political support among the electorate. For example, in the
2007 election, Labor received 43% of the primary vote while the
Coalition received 42%. This would suggest a close election, after all
the primary votes are very close between the two parties. In fact, the
result was a landslide victory for the Labor Party. The ALP received 64%
of the preference flow from other voters resulting in TPP of 52.7 of
Labor - a much clearer sign of support for the primary vote. TPP is
therefore a useful measure of the support of the major parties.

### 3.4.2. TPP in 2022 Election

In the 2022 election, the Labor party won a majority of seats
(divisions) in the house of representatives with a record low primary
vote of 32.6% (actually going backwards from the previous election they
lost), as did the Coalition on 35.7% primary vote. Many pundits leading
up to the election declared that it was not possible to form a majority
government on the back of such low primary support. In fact that Labor
won a slim majority with a TPP of 52.13%. Some pundits clearly
misunderstood the nature of preferential voting - many voters voted for
the progressive Greens Party (12.25%) and then preference the ALP above
the Coalition. On election night journalists bemoaned the demise of the
two party system, failing to realise that voters used the preferential
system to full effect for the first time. The 2022 election should be a
celebration of democracy and the fact that voters were both able to make
the primary intentions and desires for the leadership of the country
heard, while at the same time having a say of the two men with a
reasonable chance of becoming Prime Minister.

Putting aside much of the misunderstanding about the preferential system
by journalists the TPP result does have a few problems. In 2022, the
Coalition recorded a TPP of 47.87% but only 58 seats. By contrast, in
the 2007 election the Coalition had an even lower TPP of 47.3% but won
65 seats. This was first time the election was not entirely a
**two-party contest**. Independents and the Greens both recorded large
swings towards them - winning seats off both major parties, but
primarily the Coalition. The combined \"Others\" vote in the 2022
election was just below a third.

On election night, in seats such as Macnamara, Griffith and Brisbane 3
Candidate Preferred (3CP) results were calculated on election night.
Some work since has been done on 3CP contests.[^2] In all three seats,
the final 3 candidates would clearly be the Liberal Party, Labor, and
the Greens. Because Labor and the Greens have strong preference flows to
one another (both are progressive ideologically) it was clear that the
Liberals could not win any of the seats. But the order of the 3 parties
were important in determining the final winner. For example, the results
in Brisbane[^3] are displayed in Figure
[\[tab:2022Brisbane\]](#tab:2022Brisbane){reference-type="ref"
reference="tab:2022Brisbane"}. While Labor came second on primary votes,
a strong primary flow from the Animal Justice Party (AJP) to the Greens
and weak preference flows to Labor meant the Greens took second place in
the 3CP count. Labor was then eliminated from the count and Greens
elected on Labor preferences ahead of the LNP candidate. This race for
second place occurred in Macnamara (Labor eventually won) and Griffith
(Greens won). In all three cases, a simple forecasting model that
operated on TPP swing was clearly inadequate. The fact Labor started
ahead of the Greens on primary votes and that the Green's won the
election from third place shows that a forecasting model cannot be
complete without attention given to the preference system.

<div style="page-break-after: always;"></div>

# 4. Forecasting The Australian Election

The rise of the Greens a third force in Australian electoral politics,
especially in the House of Representatives presents new challenges and
exposes the complicated nature of forecasting election results. First,
Australia does not have a proportional electoral system. In many
countries like Germany and New Zealand candidates are elected through
proportional representation, which means that parties are allocated a
certain number of members in parliament proportional to the percentage
of the vote they received, (with some quirks in each system, of course).
This system has the benefit that predicting seat outcomes is easy, if an
accurate guess of the voting percentages is made. By contrast, Australia
uses a single-member electorate system. Each electorate holds its own
election, meaning that the national vote (which polls are designed to
capture) is not necessarily reflective of seat outcomes. In 1998, the
ALP received a majority in the TPP and the largest primary vote, but the
Coalition won majority government. One usual work around is to use
polling in order to calculate a national swing, how much have the
national votes changed across the nation since the previous election?
Then apply this swing to each individual electorate from the previous
electorate (this is called a uniform swing). The ABC's Antony Green
publishes a pendulum, which shows how much the TPP needs to swing in one
direction to change the government - using this uniform swing approach.
While this approach is successful in TPP contests, the growing size of
non-major parties has rendered it less useful then before. Albeit it
still remains a strong indicator of public support for/against the
government. Therefore, there needs to be a consideration of the
Australian electoral system as it really is, a preferential system
designed to accommodate multi-party democracy.

Forecasting that includes a detailed model of the preferential system is
important. First, it is reflective of the electoral system that
Australia uses and therefore, more likely to be accurate. Secondly, the
2022 election shows that as the major parties decline, the preferences
become more important. At the next election Labor could lose more votes
to the Greens but still form majority government (even gain seats). In
the wake, of Anthony Albanese's election conservative pundits declared
that the preferential voting system was unfair (failing to realise it
was originally established to prevent Labor from winning). Education
about the importance of preferences and that winning a preferential
election even with a small share is legitimate is importance for trust
in Australian democracy. And while pundits were wrong to question the
validity of the result on the back of losing an election, questions
about our system do remain. For example, what are the tangible
differences between compulsory (federal) and optional (state)
preferential voting, and do we require minimum vote shares in order to
elect candidates? For example, a candidate with only 2 primary votes
could theoretically win an election against an opponent with 1000
primary votes if 999 other voters preferenced the first candidate above
the second (and all the stars aligned in terms of other candidates vote
share). Is this a fair result or should we require, where possible, that
a minimum levels of primary vote support be required in order to be
elected. In Germany, parties are required to win 5% of the national vote
in order to win seats in the Bundestag, or win at least 3 local member
seats, with the belief that this stops extremist parties from being
unduly elected. Should Australia consider this sort of \"safeguard\"
against extremist parties?

These questions require that the public have a better understanding of
the electoral system they live in. Developing forecast and models that
then allow political journalists to provide better explanation to the
public is one way of achieving this.

## 4.1. Model Outline

Co

[^1]: Note that some Australian states use optional preferential voting,
    which I hope to model at a later date.

[^2]: https://abjago.net/3pp/

[^3]: Primaries and 2CP source:
    [https://www.abc.net.au/news/elections/federal/2022/guide/bris](url)
    3CP Source:
    [https://twitter.com/AusElectoralCom/status/1530085733905858561/photo/1](url)

<div style="page-break-after: always;"></div>

# 5. Predicting National Values

**A Side Note**: *Every model should be trained to calculate the swing from the previous election*
## 5.1. Fundamentals
Regression analysis on fundamental data is used to predict the primary votes of each of following parties:
1. Coalition
2. ALP
3. Greens
4. ONP
5. UAP
6. Independents
7. Others
These fundamentals are calculated using regression analysis of economic and other data. Preliminary data will include:
- Yearly Unemployment Data
- Quarterly Unemployment Data
- Monthly Unemployment Data
- Yearly Inflation Rate
- Quarterly Inflation Rate
- Annual discretionary spending
The regression analysis needs to be "smart" enough such that it can include the effects of the "change in" a fundamental. For example, that is to say that a government's vote share may be different if the unemployment rate is increasing/decreasing.

Research needs to be done to determine how to perform the regression analysis as "good" economic data will likely benefit the government of the day.

## 5.2. Polling Data 
The fundamentals will then be "fed" into a Kalman filter, which is then updated over time as polls are released. The filter should be designed such that as when polls are not released the filter moves back towards the fundamentals, but the more frequent the polls the less the fundamentals are weighted.
- This will be a Bayesian treatment of the polls, with consideration to the in house effect of each of the pollsters.
- Reseach will need to be done to determine the most "correct" way to implement the Kalman filter in a Bayesian way.
- Consider including prime-ministerial approval to this model as this represents an extra data point.
- Fundamentals should be updated as new data emerges.

<div style="page-break-after: always;"></div>

# 6. Testing seats
National Economic data is then used to calculated the predicted swing in each seat:
1. The seats are listed in a random order.
2. The first seat in the list has it's primary vote shifted uniformly according to the National vote predictions.
3. Every remaining seat has it's currently primary vote value shifted according to the correlation with the first seat. The results for all of the seats are stored.
4. 2 and 3 are repeated many times and then averaged. This resulting list is then normalised according to the populations in each of the seats such that the sum of the predicted votes matches the national vote projection.
Calculating 2CP and winner in each seat:
TODO

<div style="page-break-after: always;"></div>

# 7. Predicting Winner From Seat Data
TODO: Possibly a logistic regression
1. Coalition
2. ALP
3. Greens
4. ONP
5. UAP
6. Independents
7. Others
These fundamentals are calculated using regression analysis of economic and other data. Preliminary data will include:
- Yearly Unemployment Data
- Quarterly Unemployment Data
- Monthly Unemployment Data
- Yearly Inflation Rate
- Quarterly Inflation Rate
- Annual discretionary spending
The regression analysis needs to be "smart" enough such that it can include the effects of the "change in" a fundamental. For example, that is to say that a government's vote share may be different if the unemployment rate is increasing/decreasing.

Research needs to be done to determine how to perform the regression analysis as "good" economic data will likely benefit the government of the day.

## 7.1. Polling Data 
The fundamentals will then be "fed" into a Kalman filter, which is then updated over time as polls are released. The filter should be designed such that as when polls are not released the filter moves back towards the fundamentals, but the more frequent the polls the less the fundamentals are weighted.
- This will be a Bayesian treatment of the polls, with consideration to the in house effect of each of the pollsters.
- Reseach will need to be done to determine the most "correct" way to implement the Kalman filter in a Bayesian way.
- Consider including prime-ministerial approval to this model as this represents an extra data point.
- Fundamentals should be updated as new data emerges.

<div style="page-break-after: always;"></div>

# 8. Testing seats
National Economic data is then used to calculated the predicted swing in each seat:
1. The seats are listed in a random order.
2. The first seat in the list has it's primary vote shifted uniformly according to the National vote predictions.
3. Every remaining seat has it's currently primary vote value shifted according to the correlation with the first seat. The results for all of the seats are stored.
4. 2 and 3 are repeated many times and then averaged. This resulting list is then normalised according to the populations in each of the seats such that the sum of the predicted votes matches the national vote projection.
Calculating 2CP and winner in each seat:
TODO

<div style="page-break-after: always;"></div>

# 9. Predicting Winner From Seat Data
TODO: Possibly a logistic regression




