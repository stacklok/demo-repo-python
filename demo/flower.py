"""Flower ASCII art functionality for the demo application."""

FLOWERS = {
    "rose": """
    @@@@@:
   @@@@@@@@.
  @@@@@@@@@@@
  @@@@@@@@@@@@
  .@@@@@@@@@@@
   @@@@@@@@@@
    @@@@@@@@
     @@@@@
      \|/
       |
      \|/
    \\|//|\\\\
     \\\|///
""",
    "tulip": """
      /\\
     /  \\
    /    \\
   /      \\
  /        \\
  |  |  |  |
  |  |  |  |
   \\ \\/\\/ /
    \\|  |/
      ||
      ||
      ||
      ||
   ___||___
""",
    "sunflower": """
        \\\\|//
      \\\\\\|||///
     \\\\\\|||||///
    |||||||||||
     /|||||||\\
    //||||||\\\\ 
        |||
        |||
        |||
        |||
    \\\\\\///\\\\\\///
     \\\\//  \\\\//
"""
}

def print_flower(name=None):
    """Print ASCII art of a flower.
    
    Args:
        name: Name of the flower to print. If None, prints all available flowers.
        
    Returns:
        str: The ASCII art of the flower(s)
    """
    if name and name.lower() in FLOWERS:
        return FLOWERS[name.lower()]
    elif name:
        available_flowers = ", ".join(FLOWERS.keys())
        return f"Flower '{name}' not found! Available flowers: {available_flowers}"
    else:
        # Print all flowers
        result = []
        for flower_name, art in FLOWERS.items():
            result.append(f"--- {flower_name.capitalize()} ---")
            result.append(art)
        return "\n".join(result)