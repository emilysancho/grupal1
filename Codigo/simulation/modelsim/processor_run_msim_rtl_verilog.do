transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -sv -work work +incdir+C:/Users/ACER/Desktop/Arqui\ IS\ 2022/ProyectoGrupal1/grupal1/Codigo/Fetch {C:/Users/ACER/Desktop/Arqui IS 2022/ProyectoGrupal1/grupal1/Codigo/Fetch/fetch_mux.sv}
vlog -sv -work work +incdir+C:/Users/ACER/Desktop/Arqui\ IS\ 2022/ProyectoGrupal1/grupal1/Codigo/Fetch {C:/Users/ACER/Desktop/Arqui IS 2022/ProyectoGrupal1/grupal1/Codigo/Fetch/tb_fetch_mux.sv}

