# ==========================================
# 1. READ INPUT DATA FROM USER
# ==========================================
product_id = input()              # Reads Product ID as string
product_name = input()            # Reads Product Name as string
category = input()                # Reads Category as string
unit_price = float(input())       # Converts price input to float (decimal)
quantity = int(input())           # Converts current stock quantity input to integer
reorder_level = int(input())      # Converts minimum threshold reorder level to integer

# ==========================================
# 2. CREATE A TUPLE RECORD
# ==========================================
# Tuples are immutable data structures used here to group related product details
product_record = (
    product_id,
    product_name,
    category,
    unit_price,
    quantity
)

# ==========================================
# 3. ACCESSING ELEMENTS USING INDEXING
# ==========================================
indexed_product_id = product_record[0]    # Index 0 gets the 1st element (Product ID)
indexed_product_name = product_record[1]  # Index 1 gets the 2nd element (Product Name)

# ==========================================
# 4. TUPLE UNPACKING
# ==========================================
# Unpacks all elements of the tuple directly into individual variables
record_id, record_name, record_category, record_price, record_quantity = product_record

# ==========================================
# 5. CALCULATIONS
# ==========================================
# Calculates total stock value = price per unit * quantity available
stock_value = record_price * record_quantity

# ==========================================
# 6. CONDITIONAL LOGIC (STOCK STATUS)
# ==========================================
if record_quantity == 0:
    stock_status = "Out of Stock"
elif record_quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# ==========================================
# 7. OUTPUT DISPLAY WITH FORMATTING
# ==========================================
print(f"Product ID: {indexed_product_id}")
print(f"Product Name: {indexed_product_name}")
print(f"Category: {record_category}")
print(f"Unit Price: {record_price:.2f}")          # :.2f formats float to 2 decimal places
print(f"Available Quantity: {record_quantity}")
print(f"Stock Value: {stock_value:.2f}")          # :.2f formats total value to 2 decimal places
print(f"Stock Status: {stock_status}")
