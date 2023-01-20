use std::time::Instant;
use proconio::input;

fn main() {
    let timer = Instant::now();  // タイマーセット
    sub(&timer, 1.9);
}

fn sub(timer: &Instant, limit: f64) {
    while timer.elapsed().as_secs_f64() < limit {
        
    }
}