module tb_setFinalImageData();
	logic clk, we;
	logic[7:0] a; 
	logic[7:0] wd;
	
	setFinalImageData UUT(clk, we,a,wd);
	
	always #1 clk = ~clk;
	
	initial begin
		$display("setFinalImageData TB...");
		clk <= 0;
		we = 1; 
		
		#2
		a = 0;
		wd = 160;
		
		#2
		a = 1;
		wd = 177;
		
		#2
		a = 2;
		wd = 194;
		
		#2
		a = 3;
		wd = 211;
		
		#2
		a = 4;
		wd = 229;
		
		#2
		a = 5;
		wd = 246;
		
		#2
		a = 6;
		wd = 255;
		
		#2
		a = 7;
		wd = 0;

	end
	
endmodule