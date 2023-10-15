/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package clases.ventanas;

import clases.Proceso;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Queue;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author cesar
 */
public class BcpProcesos extends javax.swing.JFrame implements KeyListener {
    private EjecutarProcesos ventanaPadre;
    private Queue<Proceso> nuevos;
    private Queue<Proceso> listos;
    private Queue<Proceso> bloqueados;
    private Queue<Proceso> terminados;
    /**
     * Creates new form BcpProcesos
     */
    public BcpProcesos() {
        initComponents();
        this.setFocusable(true);
        this.addKeyListener(this);
    }
    
    public void inicializarPrograma(EjecutarProcesos ventanaPadre,
        Queue<Proceso> nuevos,Queue<Proceso> listos,Queue<Proceso> bloqueados,
        Queue<Proceso> terminados, Proceso ejecucion) {
        this.ventanaPadre = ventanaPadre;
        this.nuevos = nuevos;
        this.listos = listos;
        this.bloqueados = bloqueados;
        this.terminados = terminados;
        DefaultTableModel model = (DefaultTableModel) tblBCP.getModel();
        model.setRowCount(0);
        
        for (Proceso p : this.nuevos) {
            model.addRow(new Object[]{p.obtenerID(),"Nuevo",p.obtenerDato1()
                +p.obtenerOperacion()+p.obtenerDato2(),"N/A","N/A","N/A","N/A",
                "N/A","N/A","N/A"});
        }
        
        for (Proceso p : this.listos) {
            model.addRow(new Object[]{p.obtenerID(),"Listo",p.obtenerDato1()
                +p.obtenerOperacion()+p.obtenerDato2(),p.obtenerTiempoLlegada(),
                "N/A","N/A",p.obtenerTiempoEspera(),p.obtenerTiempoServicio(),
                p.obtenerTiempoRestante(),"N/A"});
        }
        
        for (Proceso p : this.bloqueados) {
            model.addRow(new Object[]{p.obtenerID(),"Bloqueado (" +
                p.obtenerContador() + ")",p.obtenerDato1()+p.obtenerOperacion()+
                p.obtenerDato2(),p.obtenerTiempoLlegada(),"N/A","N/A",
                p.obtenerTiempoEspera(),p.obtenerTiempoServicio(),
                p.obtenerTiempoRestante(),"N/A"});
        }
        
        for (Proceso p : this.terminados) {
            model.addRow(new Object[]{p.obtenerID(),"Terminado",p.obtenerDato1()
                +p.obtenerOperacion()+p.obtenerDato2()+" ("+
                ((p.hayError())? "Error" : p.obtenerResultado()) +")",
                p.obtenerTiempoLlegada(),p.obtenerTiempoFinalizacion(),
                p.obtenerTiempoRetorno(),p.obtenerTiempoEspera(),
                p.obtenerTiempoServicio(),p.obtenerTiempoEspera(),
                p.obtenerTiempoRestante()});
        }
        
        model.addRow(new Object[]{ejecucion.obtenerID(),"Ejecución",
            ejecucion.obtenerDato1()+ejecucion.obtenerOperacion()+
            ejecucion.obtenerDato2(),ejecucion.obtenerTiempoLlegada(),"N/A",
            "N/A",ejecucion.obtenerTiempoEspera(),"N/A",
            ejecucion.obtenerTiempoEspera(),ejecucion.obtenerTiempoRestante()});
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        lblBCPProcesos = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        tblBCP = new javax.swing.JTable();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        lblBCPProcesos.setFont(new java.awt.Font("Segoe UI", 3, 18)); // NOI18N
        lblBCPProcesos.setText("BCP Procesos");

        tblBCP.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null, null, null, null, null, null},
                {null, null, null, null, null, null, null, null, null, null},
                {null, null, null, null, null, null, null, null, null, null},
                {null, null, null, null, null, null, null, null, null, null}
            },
            new String [] {
                "ID", "Estado", "Operacion y Datos", "T. llegada", "T. Finalizacion", "T. Retorno", "T. Espera", "T. Servicio", "T. Restante en CPU", "T. Respuesta"
            }
        ));
        jScrollPane1.setViewportView(tblBCP);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 702, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblBCPProcesos))
                .addContainerGap(14, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lblBCPProcesos, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jScrollPane1))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(BcpProcesos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(BcpProcesos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(BcpProcesos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(BcpProcesos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new BcpProcesos().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel lblBCPProcesos;
    private javax.swing.JTable tblBCP;
    // End of variables declaration//GEN-END:variables

    @Override
    public void keyTyped(KeyEvent e) {
        System.out.println("KeyTyped");
        if (Character.toUpperCase(e.getKeyChar()) == 'C') {
            System.out.println("Si se preciona la C");
            this.setVisible(false);
            this.ventanaPadre.setVisible(true);
            this.ventanaPadre.procesoPausado = false;
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        System.out.println("KeyPressed");
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    @Override
    public void keyReleased(KeyEvent e) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
