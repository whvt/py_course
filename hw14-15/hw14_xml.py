import xml.etree.ElementTree as ET

tree = ET.parse("products.xml")
root = tree.getroot()

total_cost = 0.0

for product in root.findall("product"):
    price_element = product.find("price")
    quantity_element = product.find("quantity")

    if price_element is not None and quantity_element is not None:
        price_text = price_element.text
        quantity_text = quantity_element.text

        if price_text is not None and quantity_text is not None:
            try:
                price = float(price_text.strip())
                quantity = int(quantity_text.strip())
                total_cost += price * quantity
            except (ValueError, TypeError):
                print(f"Error in products data: {ET.tostring(product, encoding='unicode')}")
        else:
            print(f"Invalid or missing text data: {ET.tostring(product, encoding='unicode')}")
    else:
        print(f"Invalid structure: {ET.tostring(product, encoding='unicode')}")

print(f"Total price: {total_cost}")
