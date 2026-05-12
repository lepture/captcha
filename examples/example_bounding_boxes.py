#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CAPTCHA Bounding Box Example

This example demonstrates how to use generate_with_bounding_boxes to generate CAPTCHA images
and draw bounding boxes around each character using Pillow.

This functionality is designed to provide labeled data for machine learning projects,
computer vision training, and OCR development.
"""

from PIL import Image, ImageDraw
import os
import sys

# Add project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(project_root, 'src'))

from captcha.image import ImageCaptcha


def draw_bounding_boxes_on_captcha():
    """Generate CAPTCHA example with bounding boxes"""
    
    # Ensure examples directory exists
    os.makedirs("examples", exist_ok=True)
    
    # Create CAPTCHA generator
    captcha = ImageCaptcha(width=200, height=80)
    
    # Text to generate
    text = "ABC123"
    
    print(f"Generating CAPTCHA: {text}")
    
    # Generate CAPTCHA image and bounding box information
    image, bounding_boxes = captcha.generate_with_bounding_boxes(text)
    
    # Copy image for drawing bounding boxes
    image_with_boxes = image.copy()
    draw = ImageDraw.Draw(image_with_boxes)
    
    # Print bounding box information
    print(f"\nDetected {len(bounding_boxes)} character bounding boxes:")
    for i, bbox_info in enumerate(bounding_boxes):
        char = bbox_info['character']
        x, y, w, h = bbox_info['bbox']
        print(f"Character '{char}': Position({x}, {y}), Size({w}x{h})")
        
        # Draw bounding box on image
        # Calculate bounding box corner points
        x1, y1 = x, y
        x2, y2 = x + w, y + h
        
        # Draw red bounding box
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        
        # Add character label at top-left corner of bounding box
        draw.text((x1, max(0, y1-15)), f"{char}", fill="red")
    
    # Save original CAPTCHA
    original_path = "examples/captcha_original.png"
    image.save(original_path)
    print(f"\nOriginal CAPTCHA saved to: {original_path}")
    
    # Save CAPTCHA with bounding boxes
    boxed_path = "examples/captcha_with_boxes.png"
    image_with_boxes.save(boxed_path)
    print(f"CAPTCHA with bounding boxes saved to: {boxed_path}")
    
    return image, image_with_boxes, bounding_boxes


def analyze_character_distribution(bounding_boxes, image_width):
    """Analyze character distribution in the image"""
    print(f"\nCharacter Distribution Analysis (Image width: {image_width}px):")
    print("-" * 50)
    
    for i, bbox_info in enumerate(bounding_boxes):
        char = bbox_info['character']
        x, y, w, h = bbox_info['bbox']
        
        # Calculate character center point
        center_x = x + w // 2
        center_y = y + h // 2
        
        # Calculate relative position in image (percentage)
        relative_x = (center_x / image_width) * 100
        
        print(f"Character {i+1} '{char}':")
        print(f"  Position: ({x}, {y})")
        print(f"  Size: {w} x {h}")
        print(f"  Center: ({center_x}, {center_y})")
        print(f"  Horizontal position: {relative_x:.1f}%")
        print()


def create_multiple_examples():
    """Create multiple CAPTCHA examples"""
    # Ensure examples directory exists
    os.makedirs("examples", exist_ok=True)
    
    captcha = ImageCaptcha(width=200, height=80)
    
    # Different test texts
    test_texts = ["HELLO", "12345", "A1B2C3", "XyZ789", "CAPTCHA"]
    
    print("Generating multiple CAPTCHA examples...")
    print("=" * 60)
    
    for i, text in enumerate(test_texts):
        print(f"\nExample {i+1}: {text}")
        
        # Generate CAPTCHA
        image, bounding_boxes = captcha.generate_with_bounding_boxes(text)
        
        # Draw bounding boxes
        image_with_boxes = image.copy()
        draw = ImageDraw.Draw(image_with_boxes)
        
        for bbox_info in bounding_boxes:
            char = bbox_info['character']
            x, y, w, h = bbox_info['bbox']
            
            # Draw green bounding boxes
            draw.rectangle([x, y, x+w, y+h], outline="green", width=2)
            # Add character labels
            draw.text((x, max(0, y-15)), f"{char}", fill="green")
        
        # Save file
        filename = f"examples/example_{i+1}_{text.lower()}.png"
        image_with_boxes.save(filename)
        
        print(f"  Detected {len(bounding_boxes)} characters")
        print(f"  Saved to: {filename}")


def demonstrate_custom_colors():
    """Demonstrate custom color CAPTCHAs"""
    # Ensure examples directory exists
    os.makedirs("examples", exist_ok=True)
    
    captcha = ImageCaptcha(width=250, height=100)
    
    # Custom color configurations
    color_configs = [
        {"bg": (255, 255, 255), "fg": (0, 0, 255), "name": "Blue text on white background"},
        {"bg": (0, 0, 0), "fg": (255, 255, 0), "name": "Yellow text on black background"},
        {"bg": (240, 240, 240), "fg": (128, 0, 128), "name": "Purple text on gray background"},
    ]
    
    text = "COLOR"
    print(f"\nCustom Color CAPTCHA Examples (Text: {text}):")
    print("=" * 50)
    
    for i, config in enumerate(color_configs):
        print(f"\nConfiguration {i+1}: {config['name']}")
        
        # Generate CAPTCHA
        image, bounding_boxes = captcha.generate_with_bounding_boxes(
            text, 
            bg_color=config['bg'], 
            fg_color=config['fg']
        )
        
        # Draw bounding boxes (using contrast color)
        image_with_boxes = image.copy()
        draw = ImageDraw.Draw(image_with_boxes)
        
        # Choose bounding box color (contrast with background)
        box_color = "red" if sum(config['bg']) > 400 else "yellow"
        
        for bbox_info in bounding_boxes:
            char = bbox_info['character']
            x, y, w, h = bbox_info['bbox']
            
            draw.rectangle([x, y, x+w, y+h], outline=box_color, width=2)
            draw.text((x, max(0, y-15)), f"{char}", fill=box_color)
        
        # Save file
        filename = f"examples/color_example_{i+1}.png"
        image_with_boxes.save(filename)
        
        print(f"  Background: RGB{config['bg']}")
        print(f"  Foreground: RGB{config['fg']}")
        print(f"  Saved to: {filename}")


def main():
    """Main function"""
    print("CAPTCHA Bounding Box Example Program")
    print("=" * 60)
    
    # 1. Basic example
    print("\n1. Basic Example:")
    image, image_with_boxes, bounding_boxes = draw_bounding_boxes_on_captcha()
    
    # 2. Analyze character distribution
    analyze_character_distribution(bounding_boxes, image.width)
    
    # 3. Multiple examples
    print("\n2. Generate Multiple Examples:")
    create_multiple_examples()
    
    # 4. Custom color examples
    print("\n3. Custom Color Examples:")
    demonstrate_custom_colors()
    
    print(f"\nAll examples completed!")
    print("Generated files:")
    print("- examples/captcha_original.png (Original CAPTCHA)")
    print("- examples/captcha_with_boxes.png (With bounding boxes)")
    print("- examples/example_*.png (Multiple examples)")
    print("- examples/color_example_*.png (Color examples)")


if __name__ == "__main__":
    main()
