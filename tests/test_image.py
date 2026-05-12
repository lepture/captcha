# coding: utf-8

import os
from captcha.image import ImageCaptcha

ROOT = os.path.abspath(os.path.dirname(__file__))


def test_image_generate():
    captcha = ImageCaptcha()
    data = captcha.generate('1234')
    assert hasattr(data, 'read')


def test_save_image():
    captcha = ImageCaptcha()
    filepath = os.path.join(ROOT, 'demo.png')
    captcha.write('1234', filepath)
    assert os.path.isfile(filepath)


def test_generate_with_bounding_boxes():
    """Test the new generate_with_bounding_boxes method."""
    captcha = ImageCaptcha()
    test_chars = 'ABCD'
    
    # Test the method returns correct types
    image, bounding_boxes = captcha.generate_with_bounding_boxes(test_chars)
    
    # Check that we got an Image object
    assert hasattr(image, 'size')
    assert image.size == (captcha._width, captcha._height)
    
    # Check that we got the right number of bounding boxes
    assert len(bounding_boxes) == len(test_chars)
    
    # Check the structure of each bounding box
    for i, bbox_info in enumerate(bounding_boxes):
        assert 'character' in bbox_info
        assert 'bbox' in bbox_info
        assert bbox_info['character'] == test_chars[i]
        
        # Check bbox format (x, y, width, height)
        bbox = bbox_info['bbox']
        assert len(bbox) == 4
        x, y, w, h = bbox
        
        # All values should be non-negative integers
        assert isinstance(x, int) and x >= 0
        assert isinstance(y, int) and y >= 0
        assert isinstance(w, int) and w > 0
        assert isinstance(h, int) and h > 0
        
        # Bounding box should be within image bounds
        assert x + w <= captcha._width
        assert y + h <= captcha._height


def test_generate_with_bounding_boxes_single_char():
    """Test with single character."""
    captcha = ImageCaptcha()
    test_char = 'X'
    
    image, bounding_boxes = captcha.generate_with_bounding_boxes(test_char)
    
    assert len(bounding_boxes) == 1
    assert bounding_boxes[0]['character'] == 'X'
    assert len(bounding_boxes[0]['bbox']) == 4


def test_generate_with_bounding_boxes_custom_colors():
    """Test with custom colors."""
    captcha = ImageCaptcha()
    test_chars = 'TEST'
    bg_color = (255, 255, 255)  # White background
    fg_color = (0, 0, 0, 255)   # Black text
    
    image, bounding_boxes = captcha.generate_with_bounding_boxes(
        test_chars, bg_color=bg_color, fg_color=fg_color
    )
    
    assert len(bounding_boxes) == len(test_chars)
    for i, bbox_info in enumerate(bounding_boxes):
        assert bbox_info['character'] == test_chars[i]


def test_generate_with_bounding_boxes_stress():
    """Stress test with multiple runs to ensure consistency."""
    captcha = ImageCaptcha()
    test_chars = 'ABCD'
    
    # Run multiple times to catch any random failures
    for _ in range(20):
        image, bounding_boxes = captcha.generate_with_bounding_boxes(test_chars)
        
        # Basic validations
        assert len(bounding_boxes) == len(test_chars)
        assert image.size == (captcha._width, captcha._height)
        
        # Validate each bounding box
        for bbox_info in bounding_boxes:
            assert 'character' in bbox_info
            assert 'bbox' in bbox_info
            
            x, y, w, h = bbox_info['bbox']
            # All values should be non-negative
            assert x >= 0 and y >= 0 and w >= 0 and h >= 0
            # Bounding box should not exceed image dimensions
            assert x + w <= captcha._width
            assert y + h <= captcha._height


def test_generate_with_bounding_boxes_empty_string():
    """Test with empty string."""
    captcha = ImageCaptcha()
    
    image, bounding_boxes = captcha.generate_with_bounding_boxes("")
    
    # Should return empty list for empty string
    assert len(bounding_boxes) == 0
    assert image.size == (captcha._width, captcha._height)
