# Sample function entries
function_entries = [
    (
        "box ( circle ) → box",
        "Computes box inscribed within the circle.",
        "box(circle '<(0,0),2>') → (1.414213562373095,1.414213562373095),​(-1.414213562373095,-1.414213562373095)"
    ),
    (
        "box ( point ) → box",
        "Converts point to empty box.",
        "box(point '(1,0)') → (1,0),(1,0)"
    ),
    # Add other function entries here...
]

# Creating separate .htm files for each function
for index, entry in enumerate(function_entries, start=1):
    htm_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Function Description {index}</title>
    </head>
    <body>
    <h1>Function Description {index}</h1>
    <h2>{entry[0]}</h2>
    <p><strong>Description:</strong> {entry[1]}</p>
    <p><strong>Example(s):</strong> {entry[2]}</p>
    </body>
    </html>
    """
    # Save the HTML content to a file with .htm extension
    with open(f'function_{index}.htm', 'w', encoding='utf-8') as file:
        file.write(htm_content)
    print(f"HTM file {index} created successfully.")