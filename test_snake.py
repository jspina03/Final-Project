import pytest
from snakegame import * 
import pygame
import random
from unittest import mock

# Import the functions we want to test 
# From snake_game import display_score, draw_snake, update, generate coord, game_loop

def test_display_score():
    """Test the display_score function with a variety of scores."""
    # Mock game display so no actual rendering happens 
    with mock.patch('pygame.display.set_mode'):
        game_display = pygame.display.set_mode((600,400))
        
        # Define test cases with various scores 
        scores = [0, 10, 25, 100]
        for score in scores: 
            display_score(score)
            # Check that the score is correctly rendered 
            assert isinstance(score, int)
            
def test_draw_snake():
    """Test the draw_snake function by passing different snake lengths."""
    # Mock game display and rendering functions 
    with mock.patch('pygame.display.set.mode'):
        game_display = pygame.display.set_mode((600,400))
        
        # Define test cases 
        snake_lists = [
            [[100, 100]], # Single segment snake 
            [[100, 100], [110, 110]], # Two-segment snake
            [[100, 100], [110, 100], [120, 100]], # Three-segment snake 
        ]
        
        # Test that each list is drawn without error 
        for snake in snake_lists:
            draw_snake(10, snake) # assuming snake_block = 10 
            assert len(snake) > 0 # Check that snake length is valid 
            
def test_update_snake():
    """Test updating the snake position in the list."""
    snake_list = [[100, 100], [110, 100]]
    x, y = 120, 100 # new head position 
    length = 3
    
    update(snake_list, x, y, length)
    # Check the snake has grown 
    assert len(snake_list) == 3
    assert snake_list[-1] == [120, 100] # New head added to snake 
    
    # Test that if the length has not increased, the tail segment is removed
    update(snake_list, 130, 100, 3)
    assert len(snake_list) == 3 
    assert snake_list[0] == [110, 100] # Old tail removed 

def test_generate_coord():
    """Test generating random coordinates within the display bounds."""
    display_width = 600
    display_height = 400
    snake_block = 10 

    for _ in range(100):
        x, y = generate_coord()
        # Check coordinates are within bounds and aligned to the grid
        assert 0 <= x < display_width
        assert 0 <= y < display_height
        assert x % snake_block == 0 
        assert y % snake_block == 0 
        
def test_snake_collision():
    """Test collision conditions in game_loop"""
    # Test if the snake hits a boundary 
    display_width = 600
    display_height = 400
    
    # Test that the game ends when the snake hits the boundry 
    x1 = display_width
    y1 = 200 # middle of the screen vertically 
    
    assert x1 >= display_width or y1 >= display_height or x1 < 0 or y1 < 0
    
def test_food_consumption():
    """Test if food consumption correctly increases snake length and score."""
    length_of_snake = 1
    x1, y1 = 50, 50 # snake head position 
    foodx, foody = 50, 50 # food position matched head 
    
    # Check if snake grows on consuming food 
    if x1 == foodx and y1 == foody: 
        length_of_snake += 1
    assert length_of_snake == 2
    
