	
/**
	Unidad logica aritmetrica
*/
module alu #(parameter n=32)(
	input logic[n-1:0] A,B,
	input logic[3:0] control,
	output[n-1:0] salida );
 

	logic[n-1:0] AUXresult;

	// Códigos de la señal de control
	logic[n-1:0] r_div;
	logic[n-1:0] r_or; 
	logic[n-1:0] r_and; 
	logic[n-1:0] r_mult; 
	
	
	always @* begin
		case(control)
		4'b0000: begin AUXresult <= 0; 
				end //default
								
		4'b0001: begin AUXresult <= A + B; 
				end //suma
		
		4'b0010: begin AUXresult <= A - B; 
				end //resta
								
		4'b0100: begin AUXresult <= r_div; 
				end// division
								
		4'b0101: begin AUXresult <= r_mult; 
				end // multiplicacion
								
		4'b00110: begin AUXresult <= r_and;
				end // AND
								
		4'b0111: begin AUXresult <= r_or; 
				end // OR
		
		4'b1100: begin AUXresult	<=0;	
				end	//S	
		
							
		default: AUXresult <= 0;
		endcase
	end

	assign salida = AUXresult;


endmodule