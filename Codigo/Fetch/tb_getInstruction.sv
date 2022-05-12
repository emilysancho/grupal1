// Modelsim-ASE requires a timescale directive
// vsim -gui -l msim_transcript work.tb_getInstruction -Lf altera_mf_ver
`timescale 1 ps / 1 ps

module tb_getInstruction();
logic address_width = 8; 
logic instruction_size  = 8;

logic[7:0] a;
logic[7:0] d;
logic clk;

getInstruction #( 8, 8) UUT(clk,a,d);

initial begin 
	$display("getInstruction TB...");
	a = 0;
	clk <= 0;
	#1 clk <= ~clk;
	#1 clk <= ~clk;
	
	a = 4;
	
	#1 clk <= ~clk;
	#1 clk <= ~clk;
	
	a = 159992;
	
	#1 clk <= ~clk;
	#1 clk <= ~clk;
	
	a = 12;
	
	#1 clk <= ~clk;
	#1 clk <= ~clk;
	
	a = 16;
	
	#1 clk <= ~clk;
	#1 clk <= ~clk;

end
endmodule

