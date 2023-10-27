package clases.ventanas;

import clases.ListaProcesos;
import java.awt.Color;

public class CapturarProcesos extends javax.swing.JFrame {

    EjecutarProcesos e;
    ListaProcesos lista;
    
    public CapturarProcesos() {
        initComponents();
        this.setLocationRelativeTo(null);
        this.getContentPane().setBackground(Color.decode("#71C5E8"));

        e = new EjecutarProcesos();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        lblProcesos = new javax.swing.JLabel();
        spCantidadProcesos = new javax.swing.JSpinner();
        btnAceptar = new javax.swing.JButton();
        lblQuantum = new javax.swing.JLabel();
        spQuantum = new javax.swing.JSpinner();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        lblProcesos.setFont(new java.awt.Font("Segoe UI", 3, 24)); // NOI18N
        lblProcesos.setText("Ingresa la cantidad de procesos y");

        spCantidadProcesos.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        spCantidadProcesos.setModel(new javax.swing.SpinnerNumberModel(1, 1, null, 1));

        btnAceptar.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        btnAceptar.setText("Aceptar");
        btnAceptar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAceptarActionPerformed(evt);
            }
        });

        lblQuantum.setFont(new java.awt.Font("Segoe UI", 3, 24)); // NOI18N
        lblQuantum.setText("El valor del Quantum");

        spQuantum.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        spQuantum.setModel(new javax.swing.SpinnerNumberModel(1, 1, null, 1));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 27, Short.MAX_VALUE)
                .addComponent(lblProcesos)
                .addGap(16, 16, 16))
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(132, 132, 132)
                        .addComponent(btnAceptar, javax.swing.GroupLayout.PREFERRED_SIZE, 138, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(85, 85, 85)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(spCantidadProcesos, javax.swing.GroupLayout.PREFERRED_SIZE, 97, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(spQuantum, javax.swing.GroupLayout.PREFERRED_SIZE, 97, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addComponent(lblQuantum))))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(18, 18, 18)
                .addComponent(lblProcesos)
                .addGap(2, 2, 2)
                .addComponent(lblQuantum)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(spCantidadProcesos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(spQuantum, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnAceptar)
                .addContainerGap(83, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnAceptarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAceptarActionPerformed
        lista = new ListaProcesos((int) spCantidadProcesos.getValue());
        e.inicializarPrograma(lista.getColaProcesos(), (int) spQuantum.getValue());
        e.setVisible(true);
        this.setVisible(false);
    }//GEN-LAST:event_btnAceptarActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {

        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(CapturarProcesos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }

        java.awt.EventQueue.invokeLater(() -> {
            new CapturarProcesos().setVisible(true);
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAceptar;
    private javax.swing.JLabel lblProcesos;
    private javax.swing.JLabel lblQuantum;
    private javax.swing.JSpinner spCantidadProcesos;
    private javax.swing.JSpinner spQuantum;
    // End of variables declaration//GEN-END:variables
}
