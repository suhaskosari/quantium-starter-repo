import pandas as pd

# Read all three CSV files
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

# Combine all three into one
df = pd.concat([df0, df1, df2])

# Filter only Pink Morsels
df = df[df['product'] == 'pink morsel']

# Remove $ sign from price and convert to float
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

# Calculate sales = quantity x price
df['sales'] = df['quantity'] * df['price']

# Keep only the columns we need
df = df[['sales', 'date', 'region']]

# Save to output file
df.to_csv('data/output.csv', index=False)

print("Done! output.csv has been created.")