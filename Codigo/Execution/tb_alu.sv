module tb_alu();

logic[31:0] a;
logic[31:0] b;
logic[5:0] control;

logic[31:0] salida;

alu#(32)  UUT(a,b,control,salida);

initial begin
	a = 2;
	b = 2;
	control = 1;
	
	#5
	a = 5;
	b = 2;
	control = 2;
	
	#5
	a = 2;
	b = 4;
	control = 2;
	
	#5
	a = 2;
	b = 2;
	control = 2;

end

endmodule