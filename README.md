# README

## Running the codes
Assuming that the dataset is already downloaded and unzipped, and then only the entries with Nikkei newspaper are extracted. You should upload the dataset to the Google Drive and add additional columns to the right side of the dataset. (At least I column is required to store the results of the following codes.)

Then, you can run the following codes in the order below:
- `FinBERT_NikkeiJP25En_main.py`: Main code to do the prediction by FinBERT model. Each entries are translated into English by Google Translate API and then fed into the FinBERT model.

- `StockPriceMovementLabeling.py`: Labeling the stock price movement for the day when the news items containing the entries were published, based on the stock price data of Yahoo Finance obtained by `yfinance` library.

- `CalcAccuracy.py`: Calculate the accuracy of the prediction and mixture table.

Note that these codes are assumed to be run in the Google Colab environment because they access to the Google Spreadsheet on the Google Drive. 
The ID of the Google Spreadsheet should be changed to your own ID in all the 3 codes above.

