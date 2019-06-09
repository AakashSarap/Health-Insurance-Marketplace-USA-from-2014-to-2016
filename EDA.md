

```python
# importing the required libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
! pip install plotly --upgrade
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
```

    Requirement already up-to-date: plotly in c:\users\aakas\anaconda3\lib\site-packages (3.10.0)
    Requirement already satisfied, skipping upgrade: pytz in c:\users\aakas\anaconda3\lib\site-packages (from plotly) (2018.5)
    Requirement already satisfied, skipping upgrade: retrying>=1.3.3 in c:\users\aakas\anaconda3\lib\site-packages (from plotly) (1.3.3)
    Requirement already satisfied, skipping upgrade: decorator>=4.0.6 in c:\users\aakas\anaconda3\lib\site-packages (from plotly) (4.3.0)
    Requirement already satisfied, skipping upgrade: nbformat>=4.2 in c:\users\aakas\anaconda3\lib\site-packages (from plotly) (4.4.0)
    Requirement already satisfied, skipping upgrade: requests in c:\users\aakas\anaconda3\lib\site-packages (from plotly) (2.19.1)
    Requirement already satisfied, skipping upgrade: six in c:\users\aakas\anaconda3\lib\site-packages (from plotly) (1.11.0)
    Requirement already satisfied, skipping upgrade: jsonschema!=2.5.0,>=2.4 in c:\users\aakas\anaconda3\lib\site-packages (from nbformat>=4.2->plotly) (2.6.0)
    Requirement already satisfied, skipping upgrade: traitlets>=4.1 in c:\users\aakas\anaconda3\lib\site-packages (from nbformat>=4.2->plotly) (4.3.2)
    Requirement already satisfied, skipping upgrade: ipython-genutils in c:\users\aakas\anaconda3\lib\site-packages (from nbformat>=4.2->plotly) (0.2.0)
    Requirement already satisfied, skipping upgrade: jupyter-core in c:\users\aakas\anaconda3\lib\site-packages (from nbformat>=4.2->plotly) (4.4.0)
    Requirement already satisfied, skipping upgrade: idna<2.8,>=2.5 in c:\users\aakas\anaconda3\lib\site-packages (from requests->plotly) (2.7)
    Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in c:\users\aakas\anaconda3\lib\site-packages (from requests->plotly) (2019.3.9)
    Requirement already satisfied, skipping upgrade: urllib3<1.24,>=1.21.1 in c:\users\aakas\anaconda3\lib\site-packages (from requests->plotly) (1.23)
    Requirement already satisfied, skipping upgrade: chardet<3.1.0,>=3.0.2 in c:\users\aakas\anaconda3\lib\site-packages (from requests->plotly) (3.0.4)
    

    You are using pip version 19.0.3, however version 19.1.1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.
    


        <script type="text/javascript">
        window.PlotlyConfig = {MathJaxConfig: 'local'};
        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
        if (typeof require !== 'undefined') {
        require.undef("plotly");
        requirejs.config({
            paths: {
                'plotly': ['https://cdn.plot.ly/plotly-latest.min']
            }
        });
        require(['plotly'], function(Plotly) {
            window._Plotly = Plotly;
        });
        }
        </script>
        



```python
# Importing BenefitsCostSharing dataset

BCS_df = pd.read_csv("BenefitsCostSharing.csv")
```

    C:\Users\aakas\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py:2785: DtypeWarning: Columns (3,6,9,10,16,17,18) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)
    


```python
# Displaying the first 10 rows of our dataset

BCS_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BenefitName</th>
      <th>BusinessYear</th>
      <th>CoinsInnTier1</th>
      <th>CoinsInnTier2</th>
      <th>CoinsOutofNet</th>
      <th>CopayInnTier1</th>
      <th>CopayInnTier2</th>
      <th>CopayOutofNet</th>
      <th>EHBVarReason</th>
      <th>Exclusions</th>
      <th>...</th>
      <th>LimitUnit</th>
      <th>MinimumStay</th>
      <th>PlanId</th>
      <th>QuantLimitOnSvc</th>
      <th>RowNumber</th>
      <th>SourceName</th>
      <th>StandardComponentId</th>
      <th>StateCode</th>
      <th>StateCode2</th>
      <th>VersionNum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Routine Dental Services (Adult)</td>
      <td>2014</td>
      <td>20%</td>
      <td>NaN</td>
      <td>20%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Above EHB</td>
      <td>NaN</td>
      <td>...</td>
      <td>Dollars per Year</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>Yes</td>
      <td>68</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Dental Check-Up for Children</td>
      <td>2014</td>
      <td>20%</td>
      <td>NaN</td>
      <td>20%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Substantially Equal</td>
      <td>NaN</td>
      <td>...</td>
      <td>Visit(s) per 6 Months</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>Yes</td>
      <td>104</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Basic Dental Care - Child</td>
      <td>2014</td>
      <td>40%</td>
      <td>NaN</td>
      <td>40%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Substantially Equal</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>NaN</td>
      <td>110</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Orthodontia - Child</td>
      <td>2014</td>
      <td>50%</td>
      <td>NaN</td>
      <td>50%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Additional EHB Benefit</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>NaN</td>
      <td>111</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Major Dental Care - Child</td>
      <td>2014</td>
      <td>50%</td>
      <td>NaN</td>
      <td>50%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Substantially Equal</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>NaN</td>
      <td>112</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Basic Dental Care - Adult</td>
      <td>2014</td>
      <td>40%</td>
      <td>NaN</td>
      <td>40%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Above EHB</td>
      <td>NaN</td>
      <td>...</td>
      <td>Dollars per Year</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>Yes</td>
      <td>113</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Orthodontia - Adult</td>
      <td>2014</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>NaN</td>
      <td>114</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Major Dental Care - Adult</td>
      <td>2014</td>
      <td>50%</td>
      <td>NaN</td>
      <td>50%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Above EHB</td>
      <td>NaN</td>
      <td>...</td>
      <td>Dollars per Year</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>Yes</td>
      <td>115</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Accidental Dental</td>
      <td>2014</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21989AK0010001-00</td>
      <td>NaN</td>
      <td>118</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Routine Dental Services (Adult)</td>
      <td>2014</td>
      <td>20%</td>
      <td>NaN</td>
      <td>20%</td>
      <td>No Charge</td>
      <td>NaN</td>
      <td>No Charge</td>
      <td>Above EHB</td>
      <td>NaN</td>
      <td>...</td>
      <td>Dollars per Year</td>
      <td>NaN</td>
      <td>21989AK0010001-01</td>
      <td>Yes</td>
      <td>68</td>
      <td>HIOS</td>
      <td>21989AK0010001</td>
      <td>AK</td>
      <td>AK</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 32 columns</p>
</div>




```python
# Replacing empty records with NaN

BCS_df = BCS_df.fillna(np.nan)

# Looking for the null values

BCS_df.isnull().sum()
```




    BenefitName                  0
    BusinessYear                 0
    CoinsInnTier1          1113847
    CoinsInnTier2          4571587
    CoinsOutofNet          1113847
    CopayInnTier1          1113847
    CopayInnTier2          4571587
    CopayOutofNet          1113849
    EHBVarReason           3020737
    Exclusions             4572247
    Explanation            4075700
    ImportDate                   0
    IsCovered               215980
    IsEHB                  1817362
    IsExclFromInnMOOP       983986
    IsExclFromOonMOOP       982626
    IsStateMandate         4250463
    IsSubjToDedTier1       2465877
    IsSubjToDedTier2       2466054
    IssuerId                     0
    IssuerId2                    0
    LimitQty               4360725
    LimitUnit              4360539
    MinimumStay            5031681
    PlanId                       0
    QuantLimitOnSvc        3264532
    RowNumber                    0
    SourceName                   0
    StandardComponentId          0
    StateCode                    0
    StateCode2                   0
    VersionNum                   0
    dtype: int64




```python
# Checking the total number of rows in our dataset

len(BCS_df)
```




    5048408




```python
# Unique Benefits in the dataset

BCS_df.BenefitName.nunique()
```




    861




```python
# Summarizing our dataset

BCS_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BusinessYear</th>
      <th>IssuerId</th>
      <th>IssuerId2</th>
      <th>LimitQty</th>
      <th>MinimumStay</th>
      <th>RowNumber</th>
      <th>VersionNum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.048408e+06</td>
      <td>5.048408e+06</td>
      <td>5.048408e+06</td>
      <td>687683.000000</td>
      <td>16727.000000</td>
      <td>5.048408e+06</td>
      <td>5.048408e+06</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.015127e+03</td>
      <td>5.220360e+04</td>
      <td>5.220360e+04</td>
      <td>142.399374</td>
      <td>47.937048</td>
      <td>9.839018e+01</td>
      <td>7.637094e+00</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.563664e-01</td>
      <td>2.592498e+04</td>
      <td>2.592498e+04</td>
      <td>1723.372817</td>
      <td>5.892297</td>
      <td>2.177890e+01</td>
      <td>3.803627e+00</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.014000e+03</td>
      <td>1.004600e+04</td>
      <td>1.004600e+04</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>6.100000e+01</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.015000e+03</td>
      <td>3.253600e+04</td>
      <td>3.253600e+04</td>
      <td>1.000000</td>
      <td>48.000000</td>
      <td>8.000000e+01</td>
      <td>5.000000e+00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.015000e+03</td>
      <td>4.839600e+04</td>
      <td>4.839600e+04</td>
      <td>20.000000</td>
      <td>48.000000</td>
      <td>9.900000e+01</td>
      <td>7.000000e+00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.016000e+03</td>
      <td>7.498000e+04</td>
      <td>7.498000e+04</td>
      <td>40.000000</td>
      <td>48.000000</td>
      <td>1.170000e+02</td>
      <td>9.000000e+00</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.016000e+03</td>
      <td>9.996900e+04</td>
      <td>9.996900e+04</td>
      <td>75000.000000</td>
      <td>90.000000</td>
      <td>1.560000e+02</td>
      <td>2.400000e+01</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Benefits Year Wise

BCS_df[["BusinessYear", "BenefitName"]].groupby('BusinessYear').describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">BenefitName</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
    <tr>
      <th>BusinessYear</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014</th>
      <td>1164869</td>
      <td>496</td>
      <td>Major Dental Care - Adult</td>
      <td>18719</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>2079286</td>
      <td>517</td>
      <td>Orthodontia - Adult</td>
      <td>31269</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>1804253</td>
      <td>429</td>
      <td>Orthodontia - Adult</td>
      <td>27389</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Analyzing the benefits State wise

BCS_df[["StateCode","BenefitName"]].groupby('StateCode').count().sort_values('BenefitName')

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BenefitName</th>
    </tr>
    <tr>
      <th>StateCode</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HI</th>
      <td>6741</td>
    </tr>
    <tr>
      <th>ID</th>
      <td>27313</td>
    </tr>
    <tr>
      <th>AL</th>
      <td>28417</td>
    </tr>
    <tr>
      <th>DE</th>
      <td>31370</td>
    </tr>
    <tr>
      <th>WV</th>
      <td>32638</td>
    </tr>
    <tr>
      <th>AK</th>
      <td>41320</td>
    </tr>
    <tr>
      <th>NH</th>
      <td>44305</td>
    </tr>
    <tr>
      <th>MS</th>
      <td>46895</td>
    </tr>
    <tr>
      <th>SD</th>
      <td>47730</td>
    </tr>
    <tr>
      <th>ND</th>
      <td>48269</td>
    </tr>
    <tr>
      <th>WY</th>
      <td>48425</td>
    </tr>
    <tr>
      <th>NM</th>
      <td>56669</td>
    </tr>
    <tr>
      <th>MT</th>
      <td>58132</td>
    </tr>
    <tr>
      <th>ME</th>
      <td>61834</td>
    </tr>
    <tr>
      <th>NV</th>
      <td>62743</td>
    </tr>
    <tr>
      <th>KS</th>
      <td>64279</td>
    </tr>
    <tr>
      <th>NE</th>
      <td>66935</td>
    </tr>
    <tr>
      <th>AR</th>
      <td>68064</td>
    </tr>
    <tr>
      <th>NJ</th>
      <td>86107</td>
    </tr>
    <tr>
      <th>LA</th>
      <td>91816</td>
    </tr>
    <tr>
      <th>OR</th>
      <td>93502</td>
    </tr>
    <tr>
      <th>NC</th>
      <td>94290</td>
    </tr>
    <tr>
      <th>MO</th>
      <td>95152</td>
    </tr>
    <tr>
      <th>UT</th>
      <td>98421</td>
    </tr>
    <tr>
      <th>IA</th>
      <td>110221</td>
    </tr>
    <tr>
      <th>SC</th>
      <td>111907</td>
    </tr>
    <tr>
      <th>OK</th>
      <td>133639</td>
    </tr>
    <tr>
      <th>TN</th>
      <td>138154</td>
    </tr>
    <tr>
      <th>VA</th>
      <td>142236</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>148531</td>
    </tr>
    <tr>
      <th>MI</th>
      <td>189225</td>
    </tr>
    <tr>
      <th>GA</th>
      <td>196579</td>
    </tr>
    <tr>
      <th>AZ</th>
      <td>221612</td>
    </tr>
    <tr>
      <th>PA</th>
      <td>260866</td>
    </tr>
    <tr>
      <th>IL</th>
      <td>320533</td>
    </tr>
    <tr>
      <th>OH</th>
      <td>331045</td>
    </tr>
    <tr>
      <th>FL</th>
      <td>364742</td>
    </tr>
    <tr>
      <th>TX</th>
      <td>465164</td>
    </tr>
    <tr>
      <th>WI</th>
      <td>512587</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Unique States

State_unique = BCS_df.StateCode.unique()
State_unique
```




    array(['AK', 'AL', 'AZ', 'FL', 'GA', 'IN', 'LA', 'MO', 'MS', 'NC', 'ND',
           'NJ', 'OK', 'PA', 'SC', 'TN', 'TX', 'WI', 'WY', 'AR', 'DE', 'IL',
           'KS', 'ME', 'MI', 'MT', 'NH', 'NM', 'VA', 'WV', 'IA', 'ID', 'NE',
           'OH', 'SD', 'UT', 'NV', 'OR', 'HI'], dtype=object)




```python
# Creating a new array for Visualization

BCS_array = []
for state in State_unique:
    BCS_state = len(BCS_df[BCS_df["StateCode"]== state])
    BCS_array.append(BCS_state)

BCS_array
```




    [41320,
     28417,
     221612,
     364742,
     196579,
     148531,
     91816,
     95152,
     46895,
     94290,
     48269,
     86107,
     133639,
     260866,
     111907,
     138154,
     465164,
     512587,
     48425,
     68064,
     31370,
     320533,
     64279,
     61834,
     189225,
     58132,
     44305,
     56669,
     142236,
     32638,
     110221,
     27313,
     66935,
     331045,
     47730,
     98421,
     62743,
     93502,
     6741]




```python
BCS_new = pd.DataFrame(
        { 'State' : State_unique,
         'Count' : BCS_array
        })

BCS_new = BCS_new.sort_values("Count", ascending=False).reset_index(drop=True)

f, ax = plt.subplots(figsize=(15, 15))
ax.set_yticklabels(State_unique, rotation='horizontal', fontsize='large')
g = sb.barplot(y = BCS_new.State, x = BCS_new.Count)
plt.show
```




    <function matplotlib.pyplot.show(*args, **kw)>




![png](output_11_1.png)



```python
scl = [
    [0.0, 'rgb(255,228,225)'],
    [0.2, 'rgb(255,182,193)'],
    [0.4, 'rgb(255,174,185)'],
    [0.6, 'rgb(238,162,173)'],
    [0.8, 'rgb(205,140,149)'],
    [1.0, 'rgb(139,95,101)']
]


data = dict(type = 'choropleth',
           locations = BCS_new['State'],
           locationmode = 'USA-states',
           colorscale = scl,
            text = BCS_new['State'],
            marker = dict (line = dict(color = 'rgb(255,255,255)',width=2)),
           z = BCS_new['Count'],
           colorbar = {'title':'No of Benefit plans'})

layout = dict(title = 'Benefit Plans across different States of USA',
         geo=dict(scope = 'usa',showlakes = True,lakecolor='rgb(85,173,240)')) 

choromap2 = go.Figure(data = [data],layout=layout)
iplot(choromap2)
```


<div>
        
        
            <div id="3612a09c-8e7a-4601-a629-0c0128cdd193" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};
                    window.PLOTLYENV.BASE_URL='https://plot.ly';
                    
                if (document.getElementById("3612a09c-8e7a-4601-a629-0c0128cdd193")) {
                    Plotly.newPlot(
                        '3612a09c-8e7a-4601-a629-0c0128cdd193',
                        [{"colorbar": {"title": {"text": "No of Benefit plans"}}, "colorscale": [[0.0, "rgb(255,228,225)"], [0.2, "rgb(255,182,193)"], [0.4, "rgb(255,174,185)"], [0.6, "rgb(238,162,173)"], [0.8, "rgb(205,140,149)"], [1.0, "rgb(139,95,101)"]], "locationmode": "USA-states", "locations": ["WI", "TX", "FL", "OH", "IL", "PA", "AZ", "GA", "MI", "IN", "VA", "TN", "OK", "SC", "IA", "UT", "MO", "NC", "OR", "LA", "NJ", "AR", "NE", "KS", "NV", "ME", "MT", "NM", "WY", "ND", "SD", "MS", "NH", "AK", "WV", "DE", "AL", "ID", "HI"], "marker": {"line": {"color": "rgb(255,255,255)", "width": 2}}, "text": ["WI", "TX", "FL", "OH", "IL", "PA", "AZ", "GA", "MI", "IN", "VA", "TN", "OK", "SC", "IA", "UT", "MO", "NC", "OR", "LA", "NJ", "AR", "NE", "KS", "NV", "ME", "MT", "NM", "WY", "ND", "SD", "MS", "NH", "AK", "WV", "DE", "AL", "ID", "HI"], "type": "choropleth", "uid": "da7d2727-536b-4fe4-b14b-30e8c9220b0e", "z": [512587, 465164, 364742, 331045, 320533, 260866, 221612, 196579, 189225, 148531, 142236, 138154, 133639, 111907, 110221, 98421, 95152, 94290, 93502, 91816, 86107, 68064, 66935, 64279, 62743, 61834, 58132, 56669, 48425, 48269, 47730, 46895, 44305, 41320, 32638, 31370, 28417, 27313, 6741]}],
                        {"geo": {"lakecolor": "rgb(85,173,240)", "scope": "usa", "showlakes": true}, "title": {"text": "Benefit Plans across different States of USA"}},
                        {"showLink": false, "linkText": "Export to plot.ly", "plotlyServerURL": "https://plot.ly", "responsive": true}
                    ).then(function(){
                            
var gd = document.getElementById('3612a09c-8e7a-4601-a629-0c0128cdd193');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>

