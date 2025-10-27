import re
import sys
import os

def split_dump():
    with open('dump.sql', 'r', encoding='utf-8') as f:
        content = f.read()    
    commands = []
    current_command = ''    
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue            
        if line.upper().startswith(('INSERT', 'CREATE', 'ALTER', 'DROP', 'SET')) and current_command:
            commands.append(current_command.strip())
            current_command = line
        else:
            current_command += line + '\n'
    
    if current_command.strip():
        commands.append(current_command.strip())    
    chunk_size = 3
    for i in range(0, len(commands), chunk_size):
        chunk = commands[i:i + chunk_size]
        filename = f'chunk_{i//chunk_size:03d}.sql'        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(chunk))        
        print(f"Created {filename} with {len(chunk)} commands")
        

if __name__ == "__main__":
    split_dump()