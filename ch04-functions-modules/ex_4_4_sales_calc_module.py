SALES_TAX_RATE = .06

def calc_sales_tax(total):
    return total * SALES_TAX_RATE

def calc_sales_total_after_tax(total):
    return total * (1 + SALES_TAX_RATE)