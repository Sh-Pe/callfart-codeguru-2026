"""
NOP (0x90) Position Checker
This script checks if a binary file has 0x90 bytes at positions 39, 78, 117, etc.
Counts from position 1 (not 0).
"""

def check_nop_positions(file_path):
    """
    Check if a binary file has 0x90 at every 39th position.
    Position counting starts from 1.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        file_size = len(data)
        print(f"File: {file_path}")
        print(f"File size: {file_size} bytes")
        
        # Show first 50 bytes for debugging
        print(f"\n--- First 50 bytes of file (for debugging) ---")
        for i in range(min(50, file_size)):
            if i % 10 == 0:
                print(f"\nPos {i+1:3d}-{min(i+10, file_size):3d}: ", end="")
            print(f"{data[i]:02X} ", end="")
        print("\n")
        
        # First, find all 0x90 bytes in the file
        print(f"\n--- All 0x90 (NOP) bytes found in file ---")
        all_nops = []
        for i, byte in enumerate(data):
            if byte == 0x90:
                position = i + 1  # Convert to 1-based position
                all_nops.append(position)
                print(f"0x90 at position {position}")
        
        if not all_nops:
            print("No 0x90 bytes found in file!")
        else:
            print(f"\nTotal 0x90 bytes found: {len(all_nops)}")
        
        print(f"\n--- Checking expected NOP positions (39, 78, 117, etc.) ---")
        print("="*70)
        
        position = 38  # First position to check (counting from 1)
        nop_count = 0
        missing_count = 0
        wrong_byte_count = 0
        
        while position <= file_size:
            # Convert to 0-based index for array access
            index = position - 1
            
            byte_value = data[index]
            
            if byte_value == 0x90:
                print(f"✓ Position {position:4d}: 0x{byte_value:02X} (NOP) - CORRECT")
                nop_count += 1
            else:
                print(f"✗ Position {position:4d}: 0x{byte_value:02X} - WRONG (expected 0x90)")
                wrong_byte_count += 1
            
            position += 39
        
        print("="*70)
        print(f"\n--- Summary ---")
        print(f"Total 0x90 bytes in file: {len(all_nops)}")
        print(f"Expected NOP positions checked: {nop_count + wrong_byte_count}")
        print(f"Correct NOPs (0x90) found: {nop_count}")
        print(f"Wrong bytes at NOP positions: {wrong_byte_count}")
        
        if wrong_byte_count == 0 and nop_count > 0:
            print(f"\n✓ SUCCESS! All NOP positions are correct!")
        elif nop_count == 0:
            print(f"\n✗ FAIL! No NOPs found at expected positions.")
        else:
            print(f"\n⚠ PARTIAL! Some NOPs are missing or incorrect.")
        
        return nop_count == (nop_count + wrong_byte_count) and nop_count > 0
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=== NOP Position Checker ===\n")
    
    file_path = input("Enter the path to your binary file: ").strip()
    
    # Clean up path
    file_path = file_path.strip('"').strip("'").replace('\\', '/')
    
    print()
    check_nop_positions(file_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n!!! ERROR !!!")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n" + "="*70)
        input("\nPress Enter to close...")