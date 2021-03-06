// Modelsim-ASE requires a timescale directive
// vsim -gui -l msim_transcript work.tb_getRawImageData -Lf altera_mf_ver
`timescale 1 ps / 1 ps

module tb_getRawImageData();

logic[17:0] a;
logic[7:0] d;
logic clk;

getRawImageData UUT(clk,a,d);

initial begin 
	$display("getRawImageData TB...");
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

