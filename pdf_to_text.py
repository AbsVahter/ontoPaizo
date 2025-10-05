#!/usr/bin/env python3
"""
Скрипт для извлечения текста из PDF файла
"""

import PyPDF2
import sys
import os

def extract_text_from_pdf(pdf_path, output_path=None):
    """
    Извлекает текст из PDF файла и сохраняет в текстовый файл
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n--- СТРАНИЦА {page_num + 1} ---\n"
                text += page.extract_text()
                text += "\n"
            
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(text)
                print(f"Текст извлечен и сохранен в: {output_path}")
            else:
                print(text)
                
            return text
            
    except Exception as e:
        print(f"Ошибка при извлечении текста: {e}")
        return None

if __name__ == "__main__":
    pdf_file = "D0 - Hollow's last hope.pdf"
    
    if os.path.exists(pdf_file):
        output_file = "hollows_last_hope_text.txt"
        extract_text_from_pdf(pdf_file, output_file)
    else:
        print(f"Файл {pdf_file} не найден!")
