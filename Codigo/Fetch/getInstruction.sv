module getInstruction #(parameter ADDRESS_WIDTH = 8, parameter INSTRUCTION_SIZE = 8)
(
	input clk,
	input [17:0] address,
	output logic [7:0] data
);
						
	instruction_mem #(ADDRESS_WIDTH,INSTRUCTION_SIZE)INSTR_MEM (address, clk, data);
endmodule