transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+C:/Users/ACER/Desktop/Arqui\ IS\ 2022/ProyectoGrupal1/grupal1/Codigo/input-output {C:/Users/ACER/Desktop/Arqui IS 2022/ProyectoGrupal1/grupal1/Codigo/input-output/rawImage_mem.v}
vlog -sv -work work +incdir+C:/Users/ACER/Desktop/Arqui\ IS\ 2022/ProyectoGrupal1/grupal1/Codigo/input-output {C:/Users/ACER/Desktop/Arqui IS 2022/ProyectoGrupal1/grupal1/Codigo/input-output/getRawImageData.sv}
vlog -sv -work work +incdir+C:/Users/ACER/Desktop/Arqui\ IS\ 2022/ProyectoGrupal1/grupal1/Codigo/input-output {C:/Users/ACER/Desktop/Arqui IS 2022/ProyectoGrupal1/grupal1/Codigo/input-output/tb_getRawImageData.sv}

