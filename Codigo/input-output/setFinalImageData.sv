
/*
	CLK: Clock
	WE: Write Enable
	wA: Write Address
	wD: Write Data
*/

module setFinalImageData(input logic CLK, WE, 
						input [17:0] wA,
						input [7:0] WD
						);
						
	logic [7:0] memory [159999:0];	
	logic [17:0] wx = 18'b000000000111111111;
	
	always_ff @(posedge CLK) 
	begin
		if(WE)	
		memory[wx[7:0]] <= WD;
		$writememh("C:/Users/ACER/Desktop/Arqui IS 2022/ProyectoGrupal1/grupal1/Codigo/input-output/finalImage.img", memory);
	end
	
endmodule
