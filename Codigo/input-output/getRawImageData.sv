module getRawImageData(
	input clk,
	input [17:0] address,
	output logic [7:0] data);
						
	rawImage_mem ROM (address, clk, data);
endmodule