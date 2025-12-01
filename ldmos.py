#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# λOS Enhanced - Colored Shell with Advanced Features
import os
import time
import math
import random
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
import threading

class EnhancedλOS:
    def __init__(self):
        # Enhanced ANSI Colors with gradients
        self.colors = {
            'RST': '\033[0m',
            'BOLD': '\033[1m',
            'DIM': '\033[2m',
            'ITALIC': '\033[3m',
            'UNDERLINE': '\033[4m',
            'BLINK': '\033[5m',
            'REVERSE': '\033[7m',
            
            # Standard colors
            'BLACK': '\033[30m',
            'RED': '\033[31m',
            'GREEN': '\033[32m',
            'YELLOW': '\033[33m',
            'BLUE': '\033[34m',
            'MAGENTA': '\033[35m',
            'CYAN': '\033[36m',
            'WHITE': '\033[37m',
            
            # Bright colors
            'BR_BLACK': '\033[90m',
            'BR_RED': '\033[91m',
            'BR_GREEN': '\033[92m',
            'BR_YELLOW': '\033[93m',
            'BR_BLUE': '\033[94m',
            'BR_MAGENTA': '\033[95m',
            'BR_CYAN': '\033[96m',
            'BR_WHITE': '\033[97m',
            
            # Backgrounds
            'BG_BLACK': '\033[40m',
            'BG_RED': '\033[41m',
            'BG_GREEN': '\033[42m',
            'BG_YELLOW': '\033[43m',
            'BG_BLUE': '\033[44m',
            'BG_MAGENTA': '\033[45m',
            'BG_CYAN': '\033[46m',
            'BG_WHITE': '\033[47m',
            
            # Gradient functions
            'GRADIENT_RAINBOW': self.rainbow_gradient,
            'GRADIENT_FIRE': self.fire_gradient,
            'GRADIENT_OCEAN': self.ocean_gradient,
            'GRADIENT_FOREST': self.forest_gradient,
        }
        
        # Settings system
        self.settings = {
            'theme': 'ocean',
            'animation_speed': 0.1,
            'prompt_style': 'λ>',
            'autosave': True,
            'sound_effects': False,
            'color_mode': 'gradient',
            'auto_complete': True,
            'show_time': True,
            'quantum_mode': False,
            'dolphin_count': 3,
            'eye_type': 'single',
            'particle_effects': True,
            'trail_length': 3,
        }
        
        # Command history
        self.history = []
        self.history_index = 0
        
        # Lambda calculus memory
        self.memory = {}
        self.variables = {}
        
        # Church encodings
        self.zero = lambda f: lambda x: x
        self.succ = lambda n: lambda f: lambda x: f(n(f)(x))
        
        # Eye arts for different modes
        self.eye_arts = {
            'single': [
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⠀⡀⠀⠂⡀⢀⢰⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣐⣬⣄⣷⡀⢸⡃⡘⡸⡄⢸⠀⠀⡇⠀⢠⠀⠀⠀",
                "⠀⠀⠀⠀⠀⣠⡴⠚⢉⢍⢂⣼⣴⣿⣿⣿⣷⣷⣷⣣⣏⣆⣼⠀⠀⠄⠀⠀⠀",
                "⠀⠀⠀⢠⡞⠋⠀⡑⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣼⣆⣌⡠⢁⡤",
                "⠀⠀⣰⠋⠀⣀⣺⣾⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁",
                "⠀⡼⠁⢀⣿⣿⣿⡿⣿⡛⣿⣿⣿⡷⢸⣿⠀⠀⠀⠀⣹⣿⣿⣿⣟⠣⠀⠀⠀",
                "⡰⠁⢀⣼⣿⠟⢿⡇⠹⣿⣿⣿⠟⠀⢠⡿⠀⠀⣠⣾⡿⣿⡥⠊⠁⠀⠀⠀⠀",
                "⠁⢠⣾⠟⠁⠀⠈⠳⢿⣦⣠⣤⣦⣼⠟⠁⣠⣾⣿⣿⣟⠍⠒⠀⠠⠀⠀⠀⠀",
                "⢠⡟⠁⢀⣀⣀⣀⣀⡀⠈⣉⣉⣡⣤⣶⣿⡿⡿⡿⡻⠥⠑⡀⠀⠀⠀⠀⠀⠀",
                "⠏⡠⠚⠉⠋⢍⠋⢫⠋⠛⢹⢻⡟⠻⣟⢏⠌⢊⡌⠌⠄⠀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠘⠂⠘⠂⠿⠈⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀"
            ],
            'triple': [
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⣠⡤⠤⢤⣄⡀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠙⢷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⣿⠀⠐⠛⠛⠛⠛⠛⠛⠛⠂⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠉⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣤⣀⡀⠈⠉⠉⠉⠉⠉⠉⠁⠀⣀⣀⡤⠤⠖⠒⠋⠉⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀"
            ],
            'quantum': [
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀",
                "⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀",
                "⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀",
                "⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀",
                "⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀",
                "⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀",
                "⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀",
                "⠀⠀⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀"
            ]
        }
        
        # Quick commands 0-9
        self.quick_commands = {
            '0': 'help',
            '1': 'eye 30',
            '2': 'eye 20',
            '3': 'demo',
            '4': 'settings show',
            '5': 'settings theme ocean',
            '6': 'settings theme fire',
            '7': 'church 7',
            '8': 'clear',
            '9': 'quantum',
        }
        
        # Extended functions with complex logic
        self.functions = {
            # Visual functions
            '🐬': lambda args: self.eye_animation(args if args else [60]),
            '👁️': lambda args: self.eye_animation(args if args else [60]),
            'eye': lambda args: self.eye_animation(args if args else [60]),
            'dolphin': lambda args: self.eye_animation(args if args else [60]),
            'λ': lambda args: self.lambda_evaluator(args),
            '∫': lambda args: self.integral_visualizer(args),
            '∂': lambda args: self.derivative_visualizer(args),
            '∑': lambda args: self.summation_visualizer(args),
            
            # Mathematical functions
            'church': lambda args: self.church_converter(args),
            'ycombinator': lambda args: self.y_combinator_demo(args),
            'factorial': lambda args: self.factorial_calculator(args),
            'fibonacci': lambda args: self.fibonacci_generator(args),
            'prime': lambda args: self.prime_checker(args),
            
            # System functions
            'save': lambda args: self.save_state(args),
            'load': lambda args: self.load_state(args),
            'export': lambda args: self.export_settings(args),
            'import': lambda args: self.import_settings(args),
        }
        
        # Pupil offsets
        self.pupil_offset_x = 0
        self.pupil_offset_y = 0
        
        # Initialize with saved state if exists
        self.load_state(['auto'])
    
    def parse_args(self, args_str, default=None):
        """Parse arguments from string"""
        if not args_str:
            return [default] if default is not None else []
        
        args = []
        for arg in args_str.split():
            try:
                # Try to convert to number
                if '.' in arg:
                    args.append(float(arg))
                else:
                    args.append(int(arg))
            except:
                args.append(arg)
        return args
    
    def c(self, color_key, text=""):
        """Get ANSI color code with optional text"""
        if color_key in self.colors and callable(self.colors[color_key]):
            return self.colors[color_key](text)
        return self.colors.get(color_key, self.colors['RST']) + text
    
    def rainbow_gradient(self, text):
        """Create rainbow gradient text"""
        rainbow = ['\033[38;5;196m', '\033[38;5;202m', '\033[38;5;208m',
                  '\033[38;5;214m', '\033[38;5;220m', '\033[38;5;226m',
                  '\033[38;5;190m', '\033[38;5;154m', '\033[38;5;118m',
                  '\033[38;5;82m', '\033[38;5;46m', '\033[38;5;47m',
                  '\033[38;5;48m', '\033[38;5;49m', '\033[38;5;51m',
                  '\033[38;5;45m', '\033[38;5;39m', '\033[38;5;33m',
                  '\033[38;5;27m', '\033[38;5;21m', '\033[38;5;57m',
                  '\033[38;5;93m', '\033[38;5;129m', '\033[38;5;165m',
                  '\033[38;5;201m', '\033[38;5;200m', '\033[38;5;199m',
                  '\033[38;5;198m', '\033[38;5;197m']
        
        result = ""
        for i, char in enumerate(text):
            color = rainbow[i % len(rainbow)]
            result += f"{color}{char}"
        return result + self.colors['RST']
    
    def fire_gradient(self, text):
        """Create fire gradient text"""
        fire = ['\033[38;5;232m', '\033[38;5;52m', '\033[38;5;88m',
                '\033[38;5;124m', '\033[38;5;160m', '\033[38;5;196m',
                '\033[38;5;202m', '\033[38;5;208m', '\033[38;5;214m',
                '\033[38;5;220m', '\033[38;5;226m']
        
        result = ""
        for i, char in enumerate(text):
            color = fire[i % len(fire)]
            result += f"{color}{char}"
        return result + self.colors['RST']
    
    def ocean_gradient(self, text):
        """Create ocean gradient text"""
        ocean = ['\033[38;5;17m', '\033[38;5;18m', '\033[38;5;19m',
                 '\033[38;5;20m', '\033[38;5;21m', '\033[38;5;27m',
                 '\033[38;5;33m', '\033[38;5;39m', '\033[38;5;45m',
                 '\033[38;5;51m', '\033[38;5;87m']
        
        result = ""
        for i, char in enumerate(text):
            color = ocean[i % len(ocean)]
            result += f"{color}{char}"
        return result + self.colors['RST']
    
    def forest_gradient(self, text):
        """Create forest gradient text"""
        forest = ['\033[38;5;22m', '\033[38;5;28m', '\033[38;5;34m',
                  '\033[38;5;40m', '\033[38;5;46m', '\033[38;5;47m',
                  '\033[38;5;48m', '\033[38;5;49m', '\033[38;5;50m',
                  '\033[38;5;51m', '\033[38;5;85m']
        
        result = ""
        for i, char in enumerate(text):
            color = forest[i % len(forest)]
            result += f"{color}{char}"
        return result + self.colors['RST']
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def eye_animation(self, args):
        """Enhanced eye animation with multiple modes"""
        frames = args[0] if args and len(args) > 0 else 60
        mode = args[1] if len(args) > 1 else self.settings['eye_type']
        
        try:
            for frame in range(frames):
                self.clear_screen()
                t = frame * self.settings['animation_speed'] * 10
                
                # Dynamic header based on theme
                theme_color = {
                    'ocean': 'BR_CYAN',
                    'fire': 'BR_RED',
                    'forest': 'BR_GREEN',
                    'rainbow': 'GRADIENT_RAINBOW'
                }.get(self.settings['theme'], 'BR_CYAN')
                
                print(self.c(theme_color) + "╔" + "═" * 80 + "╗" + self.c('RST'))
                
                title = f"👁️ λ-EYE ANIMATION [{mode.upper()}] - Frame {frame+1}/{frames}"
                if self.settings['theme'] == 'rainbow':
                    colored_title = self.c('GRADIENT_RAINBOW', title.center(80))
                else:
                    colored_title = self.c('BR_WHITE', title.center(80))
                
                print(self.c(theme_color) + "║" + colored_title + self.c(theme_color) + "║" + self.c('RST'))
                print(self.c(theme_color) + "╠" + "═" * 80 + "╣" + self.c('RST'))
                
                # Create frame buffer
                buffer = [[' ' for _ in range(80)] for _ in range(24)]
                
                # Draw wave patterns (background first)
                self._draw_wave_patterns(buffer, t, 40, 12)
                
                # Draw particle effects if enabled (on background)
                if self.settings['particle_effects']:
                    self._draw_particle_effects(buffer, t, 40, 12, frame)
                
                # Draw selected eye art (overlay on background)
                self._draw_enhanced_eye(buffer, 40, 12, t, mode)
                
                # Blink logic
                blink_period = 30
                blink_duration = 2
                is_blinking = (frame % blink_period) < blink_duration
                
                # FIXED: Lambda symbol position - 4 braille symbols left from the exact center
                # The eye art's iris center appears to be around column 34-35 in the displayed output
                # Let's position it at column 34 (40-6 = 34) to be exactly in the iris center
                lambda_x = 34  # Adjusted to be in the center of the iris
                lambda_y = 12  # Vertical center
                
                dolphin_count = self.settings['dolphin_count']
                
                if not is_blinking:
                    # Draw central symbol (pupil) - FIXED: Use theme color from prompt
                    symbol = 'λ'
                    
                    if self.settings['quantum_mode']:
                        symbol = '⚛️'
                    
                    # Get the same color as used in the prompt
                    theme_colors = {
                        'ocean': 'BR_CYAN',
                        'fire': 'BR_RED',
                        'forest': 'BR_GREEN',
                        'rainbow': 'BR_MAGENTA'  # Use bright magenta for rainbow theme in eye
                    }
                    
                    lambda_color = theme_colors.get(self.settings['theme'], 'BR_CYAN')
                    
                    # Make sure we're within buffer bounds
                    if 0 <= lambda_x < 80 and 0 <= lambda_y < 24:
                        buffer[lambda_y][lambda_x] = self.c(lambda_color) + self.c('BOLD') + symbol + self.c('RST')
                    
                    # Draw rotating dolphins around the lambda symbol
                    for i in range(dolphin_count):
                        self._draw_rotating_element(buffer, t, lambda_x, lambda_y, i, dolphin_count, frame)
                
                # Render frame with border
                for y in range(24):
                    line = self.c(theme_color) + "║ " + self.c('RST')
                    for x in range(80):
                        line += buffer[y][x]
                    line += self.c(theme_color) + " ║" + self.c('RST')
                    print(line)
                
                # Footer with settings info
                print(self.c(theme_color) + "╠" + "═" * 80 + "╣" + self.c('RST'))
                
                settings_info = f"Dolphins: {dolphin_count} | Speed: {self.settings['animation_speed']:.2f}s | Theme: {self.settings['theme']}"
                if self.settings['show_time']:
                    dt = datetime.now()
                    ns = time.time_ns() % 1000000000000
                    current_time = dt.strftime("%Y-%m-%d %H:%M:%S.%f") + f"{(ns % 1000000 // 1000):03d}" + f"{(ns % 1000):03d}p"
                    settings_info += f" | Time: {current_time}"
                
                footer = settings_info.center(80)
                if self.settings['theme'] == 'rainbow':
                    colored_footer = self.c('GRADIENT_RAINBOW', footer)
                else:
                    colored_footer = self.c('BR_WHITE', footer)
                
                print(self.c(theme_color) + "║" + colored_footer + self.c(theme_color) + "║" + self.c('RST'))
                print(self.c(theme_color) + "╚" + "═" * 80 + "╝" + self.c('RST'))
                
                time.sleep(self.settings['animation_speed'])
        except Exception as e:
            print(self.c('BR_RED', f"Animation error: {e}"))
            import traceback
            traceback.print_exc()
            time.sleep(1)
    
    def _draw_enhanced_eye(self, buffer, center_x, center_y, time_val, mode):
        """Draw enhanced eye art with animation"""
        if mode not in self.eye_arts:
            mode = 'single'
        
        eye_art = self.eye_arts[mode]
        eye_height = len(eye_art)
        eye_width = len(eye_art[0])
        
        start_y = center_y - eye_height // 2
        start_x = center_x - eye_width // 2
        
        for y, line in enumerate(eye_art):
            draw_y = start_y + y
            for x, char in enumerate(line):
                draw_x = start_x + x
                if 0 <= draw_x < 80 and 0 <= draw_y < 24:
                    if char != ' ':
                        # Animated color based on theme
                        if self.settings['theme'] == 'fire':
                            wave = (math.sin(x * 0.3 + y * 0.2 + time_val * 2) + 1) / 2
                            colors = [self.c('BR_RED'), self.c('RED'), self.c('YELLOW'), 
                                     self.c('BR_YELLOW'), self.c('RED'), self.c('BR_RED')]
                        elif self.settings['theme'] == 'ocean':
                            wave = (math.sin(x * 0.2 + y * 0.15 + time_val * 1.5) + 1) / 2
                            colors = [self.c('BR_BLUE'), self.c('BLUE'), self.c('CYAN'), 
                                     self.c('BR_CYAN'), self.c('BLUE'), self.c('BR_BLUE')]
                        elif self.settings['theme'] == 'forest':
                            wave = (math.sin(x * 0.25 + y * 0.18 + time_val * 1.8) + 1) / 2
                            colors = [self.c('BR_GREEN'), self.c('GREEN'), self.c('BR_YELLOW'), 
                                     self.c('YELLOW'), self.c('GREEN'), self.c('BR_GREEN')]
                        else:  # rainbow or default
                            wave = (math.sin(x * 0.2 + y * 0.1 + time_val * 3) + 1) / 2
                            colors = [self.c('BR_MAGENTA'), self.c('MAGENTA'), self.c('BR_CYAN'),
                                     self.c('CYAN'), self.c('BR_BLUE'), self.c('BLUE')]
                        
                        color_idx = int(wave * (len(colors) - 1))
                        buffer[draw_y][draw_x] = colors[color_idx] + char + self.c('RST')
    
    def _draw_rotating_element(self, buffer, time_val, center_x, center_y, index, total, frame):
        """Draw rotating elements (dolphins or other symbols)"""
        elements = ['🐬', '🐋', '🦈', '🐟', '🐠', '🦑', '🐙', '🪼']
        quantum_elements = ['⚛️', '🔮', '🌀', '✨', '🌌', '🪐', '⭐', '☄️']
        
        if self.settings['quantum_mode']:
            elements = quantum_elements
        
        orbit_radius = 15 + math.sin(time_val * 0.5 + index) * 5
        angle = time_val * 2 + index * (2 * math.pi / total)
        
        x = int(center_x + orbit_radius * math.cos(angle))
        y = int(center_y + orbit_radius * 0.6 * math.sin(angle))
        
        if 0 <= x < 80 and 0 <= y < 24:
            element = elements[(index + frame) % len(elements)]
            theme_colors = {
                'ocean': ['BR_CYAN', 'BR_BLUE', 'CYAN'],
                'fire': ['BR_RED', 'BR_YELLOW', 'RED'],
                'forest': ['BR_GREEN', 'GREEN', 'BR_YELLOW'],
                'rainbow': ['BR_MAGENTA', 'BR_CYAN', 'BR_BLUE']
            }
            
            colors = theme_colors.get(self.settings['theme'], ['BR_CYAN', 'BR_BLUE', 'CYAN'])
            color = colors[index % len(colors)]
            
            buffer[y][x] = self.c(color) + element + self.c('RST')
            
            # Draw trail if enabled
            if self.settings['trail_length'] > 0:
                for i in range(1, self.settings['trail_length'] + 1):
                    trail_angle = angle - i * 0.2
                    trail_x = int(center_x + (orbit_radius * (1 - i*0.1)) * math.cos(trail_angle))
                    trail_y = int(center_y + (orbit_radius * 0.6 * (1 - i*0.1)) * math.sin(trail_angle))
                    
                    if 0 <= trail_x < 80 and 0 <= trail_y < 24:
                        trail_chars = ['~', '·', '.', ',']
                        trail_char = trail_chars[(index + i) % len(trail_chars)]
                        trail_color = colors[(index + i) % len(colors)]
                        buffer[trail_y][trail_x] = self.c(trail_color) + trail_char + self.c('RST')
    
    def _draw_particle_effects(self, buffer, time_val, center_x, center_y, frame):
        """Draw particle effects"""
        particle_count = 20
        for i in range(particle_count):
            radius = 5 + math.sin(time_val * 2 + i) * 15
            angle = time_val * 3 + i * 0.3
            
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * 0.5 * math.sin(angle))
            
            if 0 <= x < 80 and 0 <= y < 24:
                particles = ['∙', '∘', '⋅', '○', '●', '⋆', '✦', '✧', '❂', '❉']
                particle = particles[(i + frame) % len(particles)]
                
                # Color particles based on theme
                if self.settings['theme'] == 'fire':
                    colors = ['BR_RED', 'RED', 'YELLOW', 'BR_YELLOW']
                elif self.settings['theme'] == 'ocean':
                    colors = ['BR_BLUE', 'BLUE', 'CYAN', 'BR_CYAN']
                elif self.settings['theme'] == 'forest':
                    colors = ['BR_GREEN', 'GREEN', 'BR_YELLOW', 'YELLOW']
                else:
                    colors = ['BR_MAGENTA', 'MAGENTA', 'BR_CYAN', 'CYAN']
                
                color = colors[i % len(colors)]
                buffer[y][x] = self.c(color) + particle + self.c('RST')
    
    def _draw_wave_patterns(self, buffer, time_val, center_x, center_y):
        """Draw mathematical wave patterns"""
        for x in range(80):
            for y in range(24):
                # Calculate distance from center
                dx = (x - center_x) / 20
                dy = (y - center_y) / 15
                
                # Create interference pattern
                wave1 = math.sin(math.sqrt(dx*dx + dy*dy) * 3 - time_val * 2)
                wave2 = math.sin(dx * 4 + time_val)
                wave3 = math.cos(dy * 3 - time_val * 1.5)
                
                wave_value = (wave1 + wave2 + wave3) / 3
                
                if abs(wave_value) > 0.3:  # Threshold for drawing
                    chars = ['·', '∙', '∘', '⊙', '◉']
                    char_idx = min(int(abs(wave_value) * len(chars)), len(chars) - 1)
                    
                    # Color based on wave phase
                    phase = (wave_value + 1) / 2  # Normalize to 0-1
                    
                    if self.settings['theme'] == 'fire':
                        if phase < 0.33:
                            color = 'RED'
                        elif phase < 0.66:
                            color = 'YELLOW'
                        else:
                            color = 'BR_YELLOW'
                    elif self.settings['theme'] == 'ocean':
                        if phase < 0.33:
                            color = 'BLUE'
                        elif phase < 0.66:
                            color = 'CYAN'
                        else:
                            color = 'BR_CYAN'
                    else:
                        if phase < 0.33:
                            color = 'MAGENTA'
                        elif phase < 0.66:
                            color = 'CYAN'
                        else:
                            color = 'BR_CYAN'
                    
                    buffer[y][x] = self.c(color) + chars[char_idx] + self.c('RST')
    
    def lambda_evaluator(self, args):
        """Enhanced lambda calculus evaluator"""
        if not args:
            return self.c('BR_YELLOW', "Usage: λ <expression> or λ <function> <argument>")
        
        expr = ' '.join(map(str, args))
        
        # Check for variable assignment
        if '=' in expr:
            var_name, var_expr = expr.split('=', 1)
            var_name = var_name.strip()
            var_expr = var_expr.strip()
            
            # Store in variables
            self.variables[var_name] = var_expr
            return self.c('BR_GREEN', f"Variable '{var_name}' defined as: {var_expr}")
        
        # Check if expression uses defined variables
        for var_name, var_expr in self.variables.items():
            if var_name in expr:
                expr = expr.replace(var_name, f'({var_expr})')
        
        # Evaluate lambda expression
        try:
            # Lambda calculus expressions
            if expr.startswith('λ'):
                # Extract parameters and body
                parts = expr[1:].split('.', 1)
                if len(parts) == 2:
                    param, body = parts
                    result = f"λ{param}.{body}"
                    self.memory[expr] = result
                    return self.c('BR_CYAN', f"λ-expression: {result}")
            
            # Church numeral conversion
            if expr.isdigit():
                num = int(expr)
                church_num = self.int_to_church(num)
                int_val = self.church_to_int(church_num)
                return self.c('BR_MAGENTA', f"Church numeral {num}: converts to {int_val}")
            
            # Variable lookup
            if expr in self.variables:
                return self.c('BR_YELLOW', f"{expr} = {self.variables[expr]}")
            
            # Try evaluating as Python expression (with safety)
            # Restricted evaluation for safety
            allowed_names = {'math': math, 'sin': math.sin, 'cos': math.cos, 
                             'tan': math.tan, 'pi': math.pi, 'e': math.e}
            
            try:
                result = eval(expr, {"__builtins__": {}}, allowed_names)
                return self.c('BR_GREEN', f"{expr} = {result}")
            except ZeroDivisionError:
                return self.c('BR_RED', "Division by zero!")
            except:
                pass
            
            return self.c('BR_YELLOW', f"Expression: {expr}")
            
        except Exception as e:
            return self.c('BR_RED', f"Evaluation error: {e}")
    
    def church_converter(self, args):
        """Convert between Church numerals and integers"""
        if not args:
            return self.c('BR_YELLOW', "Usage: church <number> or church <expression>")
        
        arg = args[0]
        
        try:
            if isinstance(arg, int) or (isinstance(arg, str) and arg.isdigit()):
                num = int(arg)
                church_num = self.int_to_church(num)
                int_val = self.church_to_int(church_num)
                
                # Generate Church numeral representation
                if num == 0:
                    church_repr = "λf.λx.x"
                else:
                    church_repr = "λf.λx." + "f(" * num + "x" + ")" * num
                
                return self.c('BR_CYAN', f"Church {num} = {church_repr} → evaluates to {int_val}")
            
            else:
                # Try to parse as Church numeral
                return self.c('BR_YELLOW', f"Church numeral parsing for '{arg}' not implemented yet")
                
        except Exception as e:
            return self.c('BR_RED', f"Church conversion error: {e}")
    
    def church_to_int(self, church_num):
        """Convert Church numeral to integer"""
        return church_num(lambda x: x + 1)(0)
    
    def int_to_church(self, n):
        """Convert integer to Church numeral"""
        result = self.zero
        for _ in range(n):
            result = self.succ(result)
        return result
    
    def y_combinator_demo(self, args):
        """Demonstrate Y combinator for recursion"""
        # Y combinator: λf.(λx.f(x x))(λx.f(x x))
        y_combinator = "λf.(λx.f(x x))(λx.f(x x))"
        
        # Example: factorial using Y combinator
        factorial = f"({y_combinator})(λf.λn.if n=0 then 1 else n*f(n-1))"
        
        demo_text = f"""
{self.c('BR_CYAN', 'Y Combinator (Fixed-point combinator):')}
{self.c('BR_WHITE', y_combinator)}

{self.c('BR_CYAN', 'Example - Factorial:')}
{self.c('BR_WHITE', factorial)}

{self.c('BR_YELLOW', 'The Y combinator allows recursion in lambda calculus by finding fixed points.')}
"""
        return demo_text
    
    def factorial_calculator(self, args):
        """Calculate factorial using Church numerals"""
        if not args:
            return self.c('BR_YELLOW', "Usage: factorial <positive_integer>")
        
        try:
            n = int(args[0])
        except:
            return self.c('BR_YELLOW', "Usage: factorial <positive_integer>")
        
        if n < 0:
            return self.c('BR_RED', "Factorial is not defined for negative numbers")
        elif n > 10:
            return self.c('BR_YELLOW', "Number too large for demonstration (n ≤ 10)")
        
        # Calculate factorial
        result = 1
        calculation = []
        for i in range(1, n + 1):
            result *= i
            calculation.append(f"{i}")
        
        calc_str = " × ".join(calculation)
        
        return self.c('BR_GREEN', f"{n}! = {calc_str} = {result}")
    
    def fibonacci_generator(self, args):
        """Generate Fibonacci sequence"""
        if not args:
            count = 10
        else:
            try:
                count = int(args[0])
            except:
                count = 10
            count = min(count, 20)  # Limit to 20
        
        fib = [0, 1]
        for i in range(2, count):
            fib.append(fib[-1] + fib[-2])
        
        fib_str = ", ".join(map(str, fib[:count]))
        
        # Golden ratio approximation
        if count >= 3:
            golden_ratio = fib[-1] / fib[-2] if fib[-2] != 0 else 0
            extra = f"\n{self.c('BR_YELLOW', f'Approximation of φ (golden ratio): {golden_ratio:.10f}')}"
        else:
            extra = ""
        
        return self.c('BR_CYAN', f"Fibonacci sequence (first {count} numbers):\n") + \
               self.c('BR_GREEN', fib_str) + extra
    
    def prime_checker(self, args):
        """Check if a number is prime"""
        if not args:
            return self.c('BR_YELLOW', "Usage: prime <positive_integer>")
        
        try:
            n = int(args[0])
        except:
            return self.c('BR_YELLOW', "Usage: prime <positive_integer>")
        
        if n < 2:
            return self.c('BR_RED', f"{n} is not prime (n < 2)")
        
        is_prime = True
        divisors = []
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        
        if is_prime:
            return self.c('BR_GREEN', f"✓ {n} is a prime number")
        else:
            divisors.sort()
            divisors_str = ", ".join(map(str, divisors[:10]))
            if len(divisors) > 10:
                divisors_str += f", ... (and {len(divisors) - 10} more)"
            return self.c('BR_RED', f"✗ {n} is not prime. Divisors: {divisors_str}")
    
    def save_state(self, args):
        """Save current state to file"""
        filename = args[0] if args else 'λos_state.json'
        
        state = {
            'settings': self.settings,
            'variables': self.variables,
            'memory': self.memory,
            'history': self.history[-100:],  # Last 100 commands
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
            return self.c('BR_GREEN', f"State saved to {filename}")
        except Exception as e:
            return self.c('BR_RED', f"Save error: {e}")
    
    def load_state(self, args):
        """Load state from file"""
        if args and args[0] == 'auto':
            filename = 'λos_state.json'
        else:
            filename = args[0] if args else 'λos_state.json'
        
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            self.settings.update(state.get('settings', {}))
            self.variables.update(state.get('variables', {}))
            self.memory.update(state.get('memory', {}))
            self.history = state.get('history', [])
            
            timestamp = state.get('timestamp', 'unknown')
            return self.c('BR_GREEN', f"State loaded from {filename} (saved: {timestamp})")
        except FileNotFoundError:
            if args and args[0] != 'auto':
                return self.c('BR_YELLOW', f"File {filename} not found")
            return ""
        except Exception as e:
            return self.c('BR_RED', f"Load error: {e}")
    
    def export_settings(self, args):
        """Export settings to file"""
        filename = args[0] if args else 'λos_settings.json'
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.settings, f, indent=2)
            return self.c('BR_GREEN', f"Settings exported to {filename}")
        except Exception as e:
            return self.c('BR_RED', f"Export error: {e}")
    
    def import_settings(self, args):
        """Import settings from file"""
        filename = args[0] if args else 'λos_settings.json'
        
        try:
            with open(filename, 'r') as f:
                imported_settings = json.load(f)
            
            self.settings.update(imported_settings)
            return self.c('BR_GREEN', f"Settings imported from {filename}")
        except FileNotFoundError:
            return self.c('BR_RED', f"File {filename} not found")
        except Exception as e:
            return self.c('BR_RED', f"Import error: {e}")
    
    def settings_manager(self, args):
        """Manage system settings"""
        if not args:
            # Show current settings
            settings_text = self.c('BR_CYAN', "Current Settings:\n") + self.c('BR_WHITE')
            for key, value in self.settings.items():
                settings_text += f"  {key:20} = {value}\n"
            return settings_text
        
        # Parse setting command
        cmd = args[0].lower()
        
        if cmd == 'show':
            return self.settings_manager([])
        
        elif cmd == 'reset':
            default_settings = {
                'theme': 'ocean',
                'animation_speed': 0.1,
                'prompt_style': 'λ>',
                'autosave': True,
                'sound_effects': False,
                'color_mode': 'gradient',
                'auto_complete': True,
                'show_time': True,
                'quantum_mode': False,
                'dolphin_count': 3,
                'eye_type': 'single',
                'particle_effects': True,
                'trail_length': 3,
            }
            self.settings = default_settings
            return self.c('BR_GREEN', "Settings reset to defaults")
        
        elif cmd == 'set' and len(args) >= 3:
            key = args[1]
            value_str = args[2]
            
            if key not in self.settings:
                return self.c('BR_RED', f"Unknown setting: {key}")
            
            # Convert value to appropriate type
            old_value = self.settings[key]
            
            if isinstance(old_value, bool):
                value = value_str.lower() in ['true', 'yes', 'on', '1']
            elif isinstance(old_value, int):
                try:
                    value = int(value_str)
                except:
                    return self.c('BR_RED', f"Value must be integer for {key}")
            elif isinstance(old_value, float):
                try:
                    value = float(value_str)
                except:
                    return self.c('BR_RED', f"Value must be number for {key}")
            else:
                value = value_str
            
            self.settings[key] = value
            
            if self.settings['autosave']:
                self.save_state(['λos_state.json'])
            
            return self.c('BR_GREEN', f"Setting '{key}' changed from '{old_value}' to '{value}'")
        
        elif cmd == 'theme' and len(args) >= 2:
            theme = args[1].lower()
            valid_themes = ['ocean', 'fire', 'forest', 'rainbow']
            
            if theme in valid_themes:
                self.settings['theme'] = theme
                return self.c('BR_GREEN', f"Theme changed to '{theme}'")
            else:
                return self.c('BR_RED', f"Invalid theme. Choose from: {', '.join(valid_themes)}")
        
        else:
            return self.c('BR_YELLOW', "Usage: settings [show|reset|set <key> <value>|theme <name>]")
    
    def process_command(self, input_str):
        """Process user command with enhanced features"""
        if not input_str.strip():
            return ""
        
        # Add to history
        self.history.append(input_str)
        self.history_index = len(self.history)
        
        # Check for quick commands (0-9)
        if len(input_str) == 1 and input_str in self.quick_commands:
            input_str = self.quick_commands[input_str]
        
        # Split command and arguments
        parts = input_str.strip().split(maxsplit=1)
        cmd = parts[0]
        args_str = parts[1] if len(parts) > 1 else ""
        args = self.parse_args(args_str)
        
        # Check if command is a function
        if cmd in self.functions:
            try:
                result = self.functions[cmd](args)
                if result is not None:
                    return result
                return ""
            except Exception as e:
                return self.c('BR_RED', f"Command error: {e}")
        
        # Check for 'e' command for eye animation
        elif cmd == 'e':
            return self.eye_animation(self.parse_args(args_str, default=60))
        
        # Check for settings command
        elif cmd in ['settings', 'set', 'config']:
            return self.settings_manager(args)
        
        # Check for help command
        elif cmd == 'help':
            return self.show_help(args_str)
        
        # Check for clear command
        elif cmd == 'clear':
            self.clear_screen()
            self.show_banner()
            return ""
        
        # Check for quit command
        elif cmd in ['quit', 'exit', 'q']:
            if self.settings['autosave']:
                self.save_state(['λos_state.json'])
            print(self.c('BR_MAGENTA', "\n🌀 Farewell from Enhanced λOS! 🌌\n"))
            exit()
        
        # Check for history command
        elif cmd == 'history':
            history_text = self.c('BR_CYAN', "Command History:\n")
            for i, cmd in enumerate(self.history[-20:], 1):  # Last 20 commands
                history_text += self.c('BR_WHITE', f"  {i:3}. {cmd}\n")
            return history_text
        
        # Check for demo command
        elif cmd == 'demo':
            return self.run_demo(args)
        
        # Check for quantum command
        elif cmd == 'quantum':
            self.settings['quantum_mode'] = not self.settings['quantum_mode']
            mode = "enabled" if self.settings['quantum_mode'] else "disabled"
            return self.c('BR_MAGENTA', f"Quantum mode {mode} ✨")
        
        # Default: try as lambda expression
        else:
            return self.lambda_evaluator([input_str])
    
    def show_help(self, topic=""):
        """Show enhanced help information"""
        topic = topic.strip().lower()
        
        if topic == "quick":
            help_text = f"""
{self.c('BR_CYAN', '🚀 QUICK COMMANDS (0-9):')}

{self.c('BR_GREEN', '0')}{self.c('BR_WHITE')} - Help menu
{self.c('BR_GREEN', '1')}{self.c('BR_WHITE')} - Eye animation (30 frames)
{self.c('BR_GREEN', '2')}{self.c('BR_WHITE')} - Eye animation (20 frames)
{self.c('BR_GREEN', '3')}{self.c('BR_WHITE')} - Run demo
{self.c('BR_GREEN', '4')}{self.c('BR_WHITE')} - Show settings
{self.c('BR_GREEN', '5')}{self.c('BR_WHITE')} - Set ocean theme
{self.c('BR_GREEN', '6')}{self.c('BR_WHITE')} - Set fire theme
{self.c('BR_GREEN', '7')}{self.c('BR_WHITE')} - Church numeral 7
{self.c('BR_GREEN', '8')}{self.c('BR_WHITE')} - Clear screen
{self.c('BR_GREEN', '9')}{self.c('BR_WHITE')} - Toggle quantum mode
"""
        elif topic == "visual":
            help_text = f"""
{self.c('BR_CYAN', '👁️ VISUAL COMMANDS:')}

{self.c('BR_GREEN', '🐬 [frames] [mode]')}{self.c('BR_WHITE')} - Dolphin eye animation
{self.c('BR_GREEN', '👁️ [frames] [mode]')}{self.c('BR_WHITE')} - Same as dolphin
{self.c('BR_GREEN', 'eye [frames] [mode]')}{self.c('BR_WHITE')} - Eye animation (text alias)
{self.c('BR_GREEN', 'dolphin [frames] [mode]')}{self.c('BR_WHITE')} - Dolphin animation (text alias)
{self.c('BR_GREEN', 'e [frames] [mode]')}{self.c('BR_WHITE')} - Eye animation (short alias)
{self.c('DIM', '   Modes: single, triple, quantum')}

{self.c('BR_GREEN', 'demo')}{self.c('BR_WHITE')} - Run interactive demo
{self.c('BR_GREEN', 'quantum')}{self.c('BR_WHITE')} - Toggle quantum mode
"""
        elif topic == "math":
            help_text = f"""
{self.c('BR_CYAN', '∫ MATHEMATICAL COMMANDS:')}

{self.c('BR_GREEN', 'λ <expression>')}{self.c('BR_WHITE')} - Lambda calculus evaluator
{self.c('BR_GREEN', 'λ x=5')}{self.c('BR_WHITE')} - Define variable
{self.c('BR_GREEN', 'church <n>')}{self.c('BR_WHITE')} - Church numeral converter
{self.c('BR_GREEN', 'ycombinator')}{self.c('BR_WHITE')} - Y combinator demo
{self.c('BR_GREEN', 'factorial <n>')}{self.c('BR_WHITE')} - Calculate factorial
{self.c('BR_GREEN', 'fibonacci [n]')}{self.c('BR_WHITE')} - Generate sequence (default: 10)
{self.c('BR_GREEN', 'prime <n>')}{self.c('BR_WHITE')} - Check if number is prime
"""
        elif topic == "system":
            help_text = f"""
{self.c('BR_CYAN', '⚙️ SYSTEM COMMANDS:')}

{self.c('BR_GREEN', 'settings show')}{self.c('BR_WHITE')} - Show current settings
{self.c('BR_GREEN', 'settings set <key> <value>')}{self.c('BR_WHITE')} - Change setting
{self.c('BR_GREEN', 'settings theme <name>')}{self.c('BR_WHITE')} - Change theme
{self.c('BR_GREEN', 'settings reset')}{self.c('BR_WHITE')} - Reset to defaults
{self.c('DIM', '   Themes: ocean, fire, forest, rainbow')}

{self.c('BR_GREEN', 'save [filename]')}{self.c('BR_WHITE')} - Save state to file
{self.c('BR_GREEN', 'load [filename]')}{self.c('BR_WHITE')} - Load state from file
{self.c('BR_GREEN', 'export [filename]')}{self.c('BR_WHITE')} - Export settings
{self.c('BR_GREEN', 'import [filename]')}{self.c('BR_WHITE')} - Import settings
{self.c('BR_GREEN', 'history')}{self.c('BR_WHITE')} - Show command history
{self.c('BR_GREEN', 'clear')}{self.c('BR_WHITE')} - Clear screen
{self.c('BR_GREEN', 'quit/exit/q')}{self.c('BR_WHITE')} - Exit λOS
"""
        else:
            help_text = f"""
{self.c('BR_CYAN', '📚 ENHANCED λOS HELP - Lambda Calculus Shell:')}

{self.c('BR_YELLOW', 'Type ') + self.c('BR_GREEN', 'help <topic>') + self.c('BR_YELLOW', ' for detailed help:')}
{self.c('BR_WHITE', '  help quick    - 0-9 quick commands')}
{self.c('BR_WHITE', '  help visual   - Visual/animation commands')}
{self.c('BR_WHITE', '  help math     - Mathematical commands')}
{self.c('BR_WHITE', '  help system   - System/settings commands')}

{self.c('BR_YELLOW', 'Quick Start:')}
{self.c('BR_WHITE', '  1. Type any number 0-9 for quick actions')}
{self.c('BR_WHITE', '  2. Type ') + self.c('BR_GREEN', 'demo') + self.c('BR_WHITE', ' for guided tour')}
{self.c('BR_WHITE', '  3. Type ') + self.c('BR_GREEN', 'eye') + self.c('BR_WHITE', ' for eye animation')}
{self.c('BR_WHITE', '  4. Type ') + self.c('BR_GREEN', 'λ 2+2') + self.c('BR_WHITE', ' for calculation')}

{self.c('BR_YELLOW', 'Examples:')}
{self.c('BR_WHITE', '  λ x=5          # Define variable')}
{self.c('BR_WHITE', '  λ x*2          # Use variable')}
{self.c('BR_WHITE', '  eye 20 quantum # Quantum eye animation')}
{self.c('BR_WHITE', '  settings theme fire  # Change to fire theme')}
{self.c('BR_WHITE', '  church 3       # Show Church numeral 3')}
{self.c('BR_WHITE', '  prime 17       # Check if 17 is prime')}
"""
        
        return help_text
    
    def run_demo(self, args):
        """Run interactive demonstration"""
        demos = [
            ("eye 10", "Quick eye animation"),
            ("λ x=10", "Define variable x = 10"),
            ("λ x/2", "Calculate x/2"),
            ("church 3", "Show Church numeral 3"),
            ("prime 17", "Check if 17 is prime"),
            ("fibonacci 8", "First 8 Fibonacci numbers"),
            ("factorial 5", "Calculate 5!"),
            ("settings theme fire", "Change to fire theme"),
            ("quantum", "Toggle quantum mode"),
            ("settings show", "Show current settings"),
        ]
        
        demo_text = self.c('BR_CYAN', "🚀 Starting Enhanced λOS Demo:\n")
        
        for cmd, desc in demos:
            demo_text += f"\n{self.c('BR_YELLOW', desc)}"
            demo_text += f"\n{self.c('BR_CYAN', 'λ> ')}{self.c('BR_GREEN', cmd)}\n"
            
            result = self.process_command(cmd)
            if result:
                demo_text += f"{result}\n"
            
            time.sleep(0.3)
        
        demo_text += f"\n{self.c('BR_MAGENTA', '✨ Demo complete! Try your own commands.')}"
        return demo_text
    
    def show_banner(self):
        """Show enhanced system banner"""
        banner = f"""
{self.c('GRADIENT_RAINBOW', "╔══════════════════════════════════════════════════════════════╗")}
{self.c('GRADIENT_RAINBOW', "║")}{self.c('BR_WHITE', "           🌌 ENHANCED λOS - Lambda Calculus Shell 🌌          ")}{self.c('GRADIENT_RAINBOW', "║")}
{self.c('GRADIENT_RAINBOW', "║")}{self.c('BR_CYAN', "   Church-Turing Complete • Quantum Mode • 0-9 Quick Commands   ")}{self.c('GRADIENT_RAINBOW', "║")}
{self.c('GRADIENT_RAINBOW', "╚══════════════════════════════════════════════════════════════╝")}
{self.c('RST')}
"""
        print(banner)
    
    def get_prompt(self):
        """Get formatted prompt based on settings"""
        themes = {
            'ocean': 'BR_CYAN',
            'fire': 'BR_RED',
            'forest': 'BR_GREEN',
            'rainbow': 'BR_MAGENTA'  # For prompt, use bright magenta for rainbow theme
        }
        
        color = themes.get(self.settings['theme'], 'BR_CYAN')
        
        if self.settings['show_time']:
            dt = datetime.now()
            ns = time.time_ns() % 1000000000000
            current_time = dt.strftime("%Y-%m-%d %H:%M:%S.%f") + f"{(ns % 1000000 // 1000):03d}" + f"{(ns % 1000):03d}p"
            time_part = self.c(color) + f"[{current_time}] " + self.c('RST')
        else:
            time_part = ""
        
        prompt_style = self.settings['prompt_style']
        
        if prompt_style == 'λ>':
            prompt_symbol = self.c(color, "λ>")
        elif prompt_style == '∫>':
            prompt_symbol = self.c(color, "∫>")
        elif prompt_style == '🌀':
            prompt_symbol = self.c(color, "🌀")
        else:
            prompt_symbol = self.c(color, prompt_style)
        
        return f"{time_part}{self.c('BOLD')}{prompt_symbol}{self.c('RST')} "
    
    def integral_visualizer(self, args):
        """Placeholder for integral visualizer"""
        return self.c('BR_YELLOW', "Integral visualizer not implemented yet")
    
    def derivative_visualizer(self, args):
        """Placeholder for derivative visualizer"""
        return self.c('BR_YELLOW', "Derivative visualizer not implemented yet")
    
    def summation_visualizer(self, args):
        """Placeholder for summation visualizer"""
        return self.c('BR_YELLOW', "Summation visualizer not implemented yet")
    
    def run(self):
        """Main interactive shell"""
        self.clear_screen()
        self.show_banner()
        
        print(self.c('BR_GREEN', "🚀 Quick Start Guide:"))
        print(self.c('BR_CYAN', "• Type ") + self.c('BR_YELLOW', "0-9") + self.c('BR_CYAN', " for quick commands (0=help)"))
        print(self.c('BR_CYAN', "• Type ") + self.c('BR_YELLOW', "demo") + self.c('BR_CYAN', " for guided tour"))
        print(self.c('BR_CYAN', "• Type ") + self.c('BR_YELLOW', "help") + self.c('BR_CYAN', " for detailed help"))
        print(self.c('BR_CYAN', "• Type ") + self.c('BR_YELLOW', "eye") + self.c('BR_CYAN', " for eye animation"))
        print(self.c('BR_CYAN', "• Type ") + self.c('BR_YELLOW', "quit") + self.c('BR_CYAN', " to exit"))
        print()
        
        # Show current theme
        print(self.c('BR_MAGENTA', f"Current theme: {self.settings['theme'].upper()} | Quantum mode: {'ON' if self.settings['quantum_mode'] else 'OFF'}"))
        print()
        
        while True:
            try:
                prompt = self.get_prompt()
                user_input = input(prompt).strip()
                
                result = self.process_command(user_input)
                if result:
                    print(result)
                
            except KeyboardInterrupt:
                print(self.c('BR_RED', "\nλOS interrupted. Type 'quit' to exit."))
                print()
            except EOFError:
                print(self.c('BR_MAGENTA', "\n\n🌀 Farewell from Enhanced λOS! 🌌\n"))
                if self.settings['autosave']:
                    self.save_state(['λos_state.json'])
                exit()
            except Exception as e:
                print(self.c('BR_RED', f"Error: {e}"))

def main():
    """Main entry point"""
    try:
        os_system = EnhancedλOS()
        os_system.run()
    except KeyboardInterrupt:
        print(f"\n{EnhancedλOS().c('BR_RED')}λOS session ended.{EnhancedλOS().c('RST')}")
    except Exception as e:
        print(f"{EnhancedλOS().c('BR_RED')}Fatal error: {e}{EnhancedλOS().c('RST')}")

if __name__ == "__main__":
    main()