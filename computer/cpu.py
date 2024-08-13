from dataclasses import dataclass, field

@dataclass
class CPU:
    """
    a CHIP-8 CPU emulator
    CHIP-8 accepts CHIP-8 opcode
    an opcode consist of 16 bits, can be represent using a 4 digit hex 
    for example an opcode `0x8014` consist of 2 bytes or 16 bits
    - 8: the first digit represents opcode group, in this case, a binary operation
    - 0: the second digit represents the first register
    - 1: the third digit represents the second register
    - 4: the forth digit represents the opreation subtype, in this case, means add

    Example 1:
    >>> cpu = CPU([0]*16)
    >>> cpu.memory[0], cpu.memory[1] = 0x80, 0x14
    >>> cpu.registers[0] = 5
    >>> cpu.registers[1] = 10
    >>> cpu.run()
    >>> cpu.registers[0]
    15

    Example 2:
    >>> cpu = CPU([0]*16)
    >>> cpu.registers[0] = 5
    >>> cpu.registers[1] = 10
    >>> cpu.registers[2] = 10
    >>> cpu.registers[3] = 10
    >>> cpu.memory[0], cpu.memory[1] = 0x80, 0x14
    >>> cpu.memory[2], cpu.memory[3] = 0x80, 0x24
    >>> cpu.memory[4], cpu.memory[5] = 0x80, 0x34
    >>> cpu.run()
    >>> cpu.registers[0]
    35
    """
    registers: list[int] # 8 bit registers
    memory: list[int] = field(default_factory=lambda: [0]*4096)
    program_counter: int = 0

    def read_opcode(self) -> int:
        p = self.program_counter
        
        return self.memory[p] << 8 | self.memory[p+1] 
    
    def run(self) -> None:
        while True:
            opcode = self.read_opcode()
            # print(f"read opcode: {opcode=:04x}")
            self.program_counter += 2
            c = (opcode & 0xF000) >> 12
            x = (opcode & 0x0F00) >> 8
            y = (opcode & 0x00F0) >> 4
            d = (opcode & 0x000F) >> 0
            match c, x, y, d:
                case 0,0,0,0:
                    return
                case 0x8, _, _, 0x4:
                    self.add_xy(x, y)
                case _:
                    print(f"todo: {opcode=:04x}")
                        

    def add_xy(self, x: int, y: int):
        s = self.registers[x] + self.registers[y]
        overflow = False
        if s > 255:
            s = s & 0xFF
            overflow = True
        self.registers[x] = s
        self.registers[0xF] = 1 if overflow else 0



if __name__ == "__main__":
    cpu = CPU([0]*16)
    cpu.registers[0] = 5
    cpu.registers[1] = 10
    cpu.registers[2] = 10
    cpu.registers[3] = 10
    cpu.memory[0], cpu.memory[1] = 0x80, 0x14
    cpu.memory[2], cpu.memory[3] = 0x80, 0x24
    cpu.memory[4], cpu.memory[5] = 0x80, 0x34
    cpu.run()
    cpu.registers[0]