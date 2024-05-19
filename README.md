### MinecraftLang: An Esoteric Programming Language

MinecraftLang is a VERY BASIC esoteric programming language inspired by Minecraft - all this does is 'simulate' your inventory. This venture is of no value and it's not fully tested.

### Running Program

```
python main.py <file_name>.mine
```

### Basic Commands

- **Program Control**:
  - `PunchTree`: Start program
  - `FallInLava`: End program
- **Data Manipulation**:
  - `Mine <slot>`: Increment integer/float value in the slot
  - `Throw <slot>`: Decrement integer/float value in the slot
  - `Combine <slot_1> <slot_2>`: Add the values in two slots and store the result in the first slot and empty the second slide - if two slots have the same block type.
  - `Consume <slot_1> <value>`: Subtract the value in given slot and store in the same slot.

### Variables and Memory Management

In MinecraftLang, variables are represented using named slots in the inventory. Each slot can store a value, similar to managing an inventory in Minecraft.

- **Data Manipulation**:
  - `SetItem <slot> <block_type> <value>`: Initialize a slot with a specific material type and value.
  - `GetItem <slot>`: Retrieve the material type and value from a slot and print it.
  - `ShowInventory`: Show all variables defined till now and their values

### Sample Program

`dirt_time.mine`

```
PunchTree           # Start the program
SetItem 0 'dirt' 2  # Initialize a slot with a 2 dirt blocks
Mine 0              # Increment the value in the slot 0
Mine 0     	        # Increment the value in the slot 0
SetItem 1 'dirt' 1  # Initialize a slot with a 2 dirt blocks
Combine 0 1         # Add the values in slot 1 and 2 (4 + 1); store the value in slot 0 and empty slot 1
Consume 0 1         # Subtract 1 from slot 0 (5 - 1); store the value in slot 0
GetItem 0           # Output "You have 4 blocks of dirt"
ShowInventory       # Display your inventory
FallInLava          # End the program
```

### Helpful Learning Resources

- [Dustin Ingram The Fastest FizzBuzz in the West Make Your Own Language with RPLY and RPython ](https://youtu.be/ApgUrtCrmV8)
- Inspired by [rajiniPP](https://github.com/aadhithya/rajiniPP/tree/master)
