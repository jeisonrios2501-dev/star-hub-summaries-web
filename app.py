from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    dirigentes = ["Fabián", "Geordanny", "Maycol", "Luis", "Rosmel"]
    
    libros = [
        {
            "id": 1,
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "color": "#d97706",
            "resumen": "La obra cumbre del realismo mágico sigue las vicisitudes de siete generaciones de la familia Buendía en el pueblo caribeño de Macondo, fundado por el patriarca José Arcadio Buendía. La trama avanza entre revoluciones civiles lideradas por el Coronel Aureliano, obsesiones alquímicas, amores incestuosos marcados por el temor a una profecía (un hijo con cola de cerdo) y la inevitable soledad que destruye a cada miembro. Finalmente, el último Aureliano descifra los pergaminos de Melquíades justo cuando un torbellino bíblico borra para siempre a Macondo de la historia de la humanidad."
        },
        {
            "id": 2,
            "titulo": "Noches blancas",
            "autor": "Fiódor Dostoyevski",
            "color": "#1e3a8a",
            "resumen": "Ambientada en el San Petersburgo del siglo XIX, la novela se desarrolla durante las luminosas noches de verano rusas. El protagonista, un joven solitario que vive sumergido en sus propias fantasías románticas, camina por los puentes de la ciudad hasta que se topa con Nástenka, una chica que llora esperando al amor de su vida. A lo largo de cuatro noches de intensas e íntimas conversaciones, él se enamora profundamente de ella mientras sanan sus soledades mutuas. Sin embargo, el regreso del antiguo amante destruye la ilusión, dejando al soñador agradecido por haber conocido, al menos, un minuto completo de felicidad."
        },
        {
            "id": 3,
            "titulo": "El principito",
            "autor": "Antoine de Saint-Exupéry",
            "color": "#0284c7",
            "resumen": "Un aviador sufre una avería en medio del inhóspito desierto del Sahara y se encuentra inesperadamente con un pequeño príncipe venido del asteroide B 612. A través de sus relatos, descubrimos que el niño abandonó su hogar para explorar el universo, visitando extraños planetas habitados por adultos absurdos (un rey, un vanidoso, un geógrafo). Tras llegar a la Tierra, entabla amistad con un zorro que le enseña el secreto más profundo de la existencia: 'Lo esencial es invisible a los ojos'. Una crítica poética sobre cómo los adultos pierden la inocencia y el valor de los lazos verdaderos."
        },
        {
            "id": 4,
            "titulo": "Orgullo y prejuicio",
            "autor": "Jane Austen",
            "color": "#db2777",
            "resumen": "En la clasista Inglaterra rural, la señora Bennet busca obsesivamente casar a sus cinco hijas para asegurar su futuro financiero. La historia se centra en la audaz y perspicaz Elizabeth Bennet, quien choca de inmediato con el altivo, rico y aristocrático Fitzwilliam Darcy. Lo que sigue es un fascinante juego psicológico donde Elizabeth juzga erróneamente a Darcy basándose en las apariencias (prejuicio), mientras que Darcy lucha contra sus propios sentimientos por considerarla de clase inferior (orgullo). Tras superar escándalos familiares y malentendidos, ambos reconocen sus fallas morales y se rinden ante un amor genuino."
        },
        {
            "id": 5,
            "titulo": "El perfume",
            "autor": "Patrick Süskind",
            "color": "#7f1d1d",
            "resumen": "Jean-Baptiste Grenouille nace entre la basura de un mercado de París en el siglo XVIII sin poseer ningún olor propio corporal, pero bendecido con el sentido del olfato más perfecto del mundo. Tras pasar una infancia miserable y aprender el oficio de la perfumería, se convierte en un genio de las fragancias. Su obsesión pronto toma un rumbo macabro: capturar de forma permanente la esencia vital y olfativa de mujeres jóvenes y hermosas para crear el perfume absoluto. Tras cometer una serie de atroces crímenes, logra elaborar una esencia tan sublime que le otorga el poder de manipular el amor y la adoración de toda la humanidad, con consecuencias fatales para sí mismo."
        },
        {
            "id": 6,
            "titulo": "Don Quijote de la Mancha",
            "autor": "Miguel de Cervantes",
            "color": "#b45309",
            "resumen": "Alonso Quijano es un hidalgo pobre que, tras devorar obsesivamente novelas de caballerías, pierde el juicio y se convence de que debe salir al mundo a defender a los desvalidos como un caballero andante. Rebautizado como Don Quijote de la Mancha, recluta a su vecino, el simplón pero leal Sancho Panza, prometiéndole el gobierno de una ínsula. Juntos viven situaciones icónicas como la batalla contra los molinos de viento (que el Quijote jura que son gigantes mágicos) o la idealización de la labradora Aldonza Lorenzo como la gran dama Dulcinea del Toboso. Una profunda sátira que oscila entre la locura idealista y la cruda realidad del mundo real."
        },
        {
            "id": 7,
            "titulo": "Guerra y Paz",
            "autor": "León Tolstói",
            "color": "#15803d",
            "resumen": "Esta titánica epopeya narra la vida de cinco familias de la aristocracia rusa (los Rostov, los Bolkonsky, los Bezukhov, entre otros) cuyas existencias se ven alteradas dramáticamente por la invasión de las tropas de Napoleón Bonaparte en 1812. A través de batallas históricas memorables y bailes de alta sociedad, seguimos la transformación espiritual del torpe y rico Pierre Bezukhov, el heroísmo trágico del príncipe Andréi y la vitalidad desbordante de la joven Natasha Rostova. Tolstói ofrece una visión filosófica total sobre cómo el destino colectivo de una nación arrastra las vidas individuales, combinando la crudeza de la guerra con la intimidad familiar."
        },
        {
            "id": 8,
            "titulo": "Crimen y castigo",
            "autor": "Fiódor Dostoyevski",
            "color": "#4338ca",
            "resumen": "Rodión Raskólnikov, un exestudiante brillante sumido en la extrema pobreza en San Petersburgo, concibe una teoría psicológica: existen hombres 'extraordinarios' (como Napoleón) con el derecho moral de quebrantar las leyes por un bien mayor. Para probar su hipótesis, asesina brutalmente con un hacha a una anciana usurera. Aunque el crimen parece perfecto, Raskólnikov cae en una espiral destructiva de fiebre, culpa y paranoia, viéndose acosado por el astuto inspector Porfiri Petróvich. Solo a través del sacrificio y amor puro de Sonia, una joven obligada a prostituirse por su familia, Rodión encuentra el camino hacia el arrepentimiento y la redención en Siberia."
        },
        {
            "id": 9,
            "titulo": "Moby Dick",
            "autor": "Herman Melville",
            "color": "#0369a1",
            "resumen": "El joven marinero Ishmael decide embarcarse en el Pequod, un barco ballenero comandado por el enigmático Capitán Ahab. Pronto descubre que la misión principal del viaje no es el comercio, sino una venganza demencial armada por el capitán contra Moby Dick, una gigantesca ballena blanca que años atrás le mutiló una pierna. Desoyendo los presagios funestos de la tripulación y los sensatos consejos de su primer oficial Starbuck, Ahab arrastra al barco a una implacable persecución por los mares del mundo. La obra es una colosal alegoría sobre la obsesión humana autodestructiva, el poder incontrolable de la naturaleza salvaje y el enfrentamiento directo contra el propio destino."
        },
        {
            "id": 10,
            "titulo": "Ulises",
            "autor": "James Joyce",
            "color": "#6d28d9",
            "resumen": "Inspirada libremente en la Odisea de Homero, la novela rompe todos los moldes tradicionales de la literatura al narrar detalladamente los acontecimientos ordinarios de la vida de Leopold Bloom, un agente de publicidad judío, durante un solo día común (el 16 de junio de 1904) en las calles de Dublín. El viaje incluye sus almuerzos, sus encuentros en la prensa, entierros y visitas a burdeles, entrelazando su camino con el del joven poeta Stephen Dedalus y la infidelidad de su esposa Molly Bloom. Mediante el uso vanguardista del flujo de conciencia, Joyce expone sin filtros los pensamientos más íntimos, miedos y deseos del ser humano ordinario."
        }
    ]
    return render_template('index.html', libros=libros, dirigentes=dirigentes)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)