"""
Given two dictionaries, this benchmark calculates the sum of all values.
:param sales_today: A dictionary with products and costs.
:type  sales_today: dict
:param sales_yesterday: A dictionary with products and costs.
:type  sales_yesterday: dict
:rtype: int

{
    "benchmark_name": "GetProfit",
    "benchmark_metadata": [
        {
            "Function": ["get_profit"],
            "Bug": [ {"Position": 24, "LOC": "for cost in sales_today:"} ],
            "Fix": [ {"Position": 24, "LOC": "for cost in sales_today.values():"} ]
        }
    ]
}
"""
def get_profit1(sales_today: dict, sales_yesterday: dict) -> int:
    '''Given two dictionaries, this benchmark calculates the sum of all its values.'''
    accom: \
    int = 0

    for cost in sales_yesterday.values():
        accom += cost

    for cost in sales_today.values():
        accom += cost

    return accom



if __name__ == "__main__":
    print(get_profit1({"fd3":87},{"fd3":87}))

    print(get_profit1({"fd3":222, "grrt5":445, "ffdf4": 32},{"swd8":12, "sw34":23}))