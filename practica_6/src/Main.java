import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

// Clase que representa el contenedor de panes
class Contenedor {

    private final int capacidad = 35;
    private BlockingQueue<String> buffer = new ArrayBlockingQueue<>(capacidad);
    private final Lock lock = new ReentrantLock();
    private final Condition espacioDisponible = lock.newCondition();
    private final Condition productosDisponibles = lock.newCondition();
    private Ventana ventana;
    private int cantidadPanes = 0;

    public Contenedor(Ventana ventana) {
        this.ventana = ventana;
    }

    // Método para que el panadero produzca pan
    public void producir(String pan) throws InterruptedException {
        lock.lock(); // Adquiere el cerrojo para controlar el acceso
        try {
            if (cantidadPanes == capacidad) {
                System.out.println("El contenedor está lleno. El panadero está esperando para producir.");
                espacioDisponible.await();
            }
            buffer.put(pan);
            cantidadPanes++;
            productosDisponibles.signal();
            ventana.mostrarPan();
        } finally {
            lock.unlock(); // Libera el cerrojo después de su uso
        }
    }

    // Método para que el cliente compre pan
    public String consumir() throws InterruptedException {
        lock.lock(); // Adquiere el cerrojo para controlar el acceso
        try {
            if (cantidadPanes == 0) {
                System.out.println("El contenedor está vacío. El cliente está esperando a que se produzca pan.");
                productosDisponibles.await();
            }
            String pan = buffer.take();
            cantidadPanes--;
            espacioDisponible.signal();
            ventana.quitarPan();
            System.out.println("Cliente comprando: " + pan);
            return pan;
        } finally {
            lock.unlock(); // Libera el cerrojo después de su uso
        }
    }
}

// Clase que representa la ventana de la panadería
class Ventana extends JFrame {

    private JPanel panel;
    private int cantidadPanes = 0;

    public Ventana() {
        super("Panaderia");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 400);
        setLocationRelativeTo(null);
        panel = new JPanel();
        add(panel);
        setVisible(true);

        addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                // No se usa en este contexto
            }

            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
                    System.exit(0);
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                // No se usa en este contexto
            }
        });

        setFocusable(true);
        requestFocusInWindow();
    }

    // Método para mostrar un pan en la ventana
    public void mostrarPan() {
        SwingUtilities.invokeLater(() -> {
            // Carga la imagen de pan
            ImageIcon icon = new ImageIcon("src/imagenes/pan.png");
            JLabel panLabel = new JLabel(icon);
            panLabel.setPreferredSize(new Dimension(64, 64));
            panel.add(panLabel);
            panel.revalidate();
            panel.repaint();
            cantidadPanes++;
        });
    }

    // Método para quitar un pan de la ventana
    public void quitarPan() {
        SwingUtilities.invokeLater(() -> {
            if (cantidadPanes > 0) {
                Component[] components = panel.getComponents();
                if (components.length > 0) {
                    panel.remove(components[components.length - 1]);
                    panel.revalidate();
                    panel.repaint();
                    cantidadPanes--;
                }
            }
        });
    }
}

// Clase que representa al panadero
class Panadero extends Thread {

    private Contenedor contenedor;

    public Panadero(Contenedor contenedor) {
        this.contenedor = contenedor;
    }

    @Override
    public void run() {
        while (true) {
            try {
                int tiempoDeTrabajo = (int) (Math.random() * 2000);
                System.out.println("Panadero trabajando");
                Thread.sleep(tiempoDeTrabajo);

                String pan = hornearPan();
                System.out.println("Panadero ha producido un pan: " + pan);
                contenedor.producir(pan);
                if (Math.random() < 0.4) {
                    int tiempoDeDescanso = 500 + (int) (Math.random() * 1500);
                    System.out.println("Panadero descansando");
                    Thread.sleep(tiempoDeDescanso);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // Método para hornear un tipo de pan aleatorio
    private String hornearPan() {
        String[] tiposDePan = {"Pan de maíz", "Pan integral", "Pan de centeno", "Pan de avena", "Pan de trigo"};
        Random random = new Random();
        int index = random.nextInt(tiposDePan.length);
        return tiposDePan[index];
    }
}

// Clase que representa al cliente
class Cliente extends Thread {

    private Contenedor contenedor;

    public Cliente(Contenedor contenedor) {
        this.contenedor = contenedor;
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(1000 + (int) (Math.random() * 2000)); // Agrega un delay más largo
                System.out.println("Cliente quiere comprar");
                contenedor.consumir();

                if (Math.random() < 0.1) {
                    int tiempoDeDescanso = 500 + (int) (Math.random() * 1500);
                    System.out.println("Cliente descansando");
                    Thread.sleep(tiempoDeDescanso);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class Main {

    public static void main(String[] args) {
        Ventana ventana = new Ventana();
        Contenedor contenedor = new Contenedor(ventana);
        Panadero panadero = new Panadero(contenedor);
        Cliente cliente = new Cliente(contenedor);

        panadero.start();
        cliente.start();
    }
}
