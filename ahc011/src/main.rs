use std::time::Instant;
fn main() {  // タイマーセット
    let timer = Instant::now();
    let mut b=1;
	for i in 2..151850000 {
        b=0;
    }
    println!("Calculation time={}[s]",timer.elapsed().as_secs_f64())
}