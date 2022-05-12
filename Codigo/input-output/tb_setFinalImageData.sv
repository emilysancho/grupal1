module tb_setFinalImageData();
	logic clk, we;
	logic[17:0] a; 
	logic[7:0] wd;
	
	setFinalImageData UUT(clk, we,a,wd);
	
	always #1 clk = ~clk;
	always #2 begin a = a + 1; wd = wd + 1; end
	
	
	initial begin
		$display("setFinalImageData TB...");
		clk <= 0;
		a= 0; 
		we = 1; 
		wd =1;
		

		
	end
	
endmodule