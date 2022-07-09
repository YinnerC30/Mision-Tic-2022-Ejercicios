public class BecaUniversitaria {
    
    private int tiempo;
    private double monto;
    private double interes;

    
    public BecaUniversitaria() {
        tiempo = 0;
        monto = 0;
        interes = 0;
    }

    
    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres) {
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;
    }

    public double calcularInteresSimple() {
        double interesSimple = Math.round(monto * (interes/100) * tiempo);
        return interesSimple;
    }

    public double calcularInteresCompuesto() {
        double potencia = Math.pow( (1 + (interes/100)), tiempo);
        double interesCompuesto = Math.round(monto * (potencia - 1));
        return interesCompuesto;
    }

    public String compararInversion(int pTiempo, double pMonto, double pInteres ) {
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        }
        else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }
    

    public String compararInversion() {
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        }
        else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }

    }

}
