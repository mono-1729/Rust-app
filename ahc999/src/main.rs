use std::time::Instant;
use proconio::input;
use std::cmp::{min,max};
use rand::prelude::*;
use itertools::Itertools;
fn main() {
    let timer = Instant::now();  // タイマーセット
    sub(&timer, 1.9);
}

fn sub(timer: &Instant, limit: f64) {
    let mut rng = rand::thread_rng();
    input! {
        n:usize,
        xyr:[[usize;3];n]
    }
    let mut place=vec![vec![0;4];n];
    let mut act=vec![vec![0,0],vec![1,0],vec![2,2],vec![3,2],];
    let mut ans=0;
    for i in 0..n{
        place[i][0]=xyr[i][0];
        place[i][1]=xyr[i][1];
        place[i][2]=xyr[i][0]+1;
        place[i][3]=xyr[i][1]+1;
    }
    while timer.elapsed().as_secs_f64() < limit {
        let mut bool=true;
        let num = rng.gen::<usize>() % 4;  
        let num2 = rng.gen::<usize>() % n;  
        place[num2][act[num][0]]+=act[num][1]-1;
        if place[num2][act[num][0]]>9999{
            place[num2][act[num][0]]-=act[num][1]-1;
            continue;
        }
        for i in 0..n{
            if i==num2{
                continue
            }
            for j in 0..4{
                let x=place[i][(j/2)*2];
                let y=place[i][(j%2)*2+1];
                if place[num2][0]<=x &&place[num2][2]>=x&&place[num2][1]<=y&&place[num2][3]>=y{
                    if place[num2][0]<x ||place[num2][2]>x || place[num2][1]>y || place[num2][3]>=y{
                        bool=false;
                    }
                }
            }
            for j in 0..4{
                let x=place[num2][(j/2)*2];
                let y=place[num2][(j%2)*2+1];
                if place[i][0]<=x &&place[i][2]>=x&&place[i][1]<=y&&place[i][3]>=y{
                    if place[i][0]<x ||place[i][2]>x || place[i][1]>y || place[i][3]>=y{
                        bool=false;
                    }
                }
            }
            if !bool{
                break;
            }
        }
        if bool{
            let mut point=calc(&xyr,&place,n);
            if point>=ans{
                ans=point;
            }else{
                place[num2][act[num][0]]-=act[num][1]-1;
            }
        }else{
            place[num2][act[num][0]]-=act[num][1]-1;
        }
    }
    for i in 0..n{
        println!("{} {} {} {}",place[i][0],place[i][1],place[i][2],place[i][3])
    }
}
fn calc (xyr:&Vec<Vec<usize>>,place:&Vec<Vec<usize>>,n:usize)->i32{
    let mut point=0;
    for i in 0..n{
        point+=(min(xyr[i][2],(place[i][2]-place[i][0])*(place[i][3]-place[i][1]))*1000)/max(xyr[i][2],(place[i][2]-place[i][0])*(place[i][3]-place[i][1]))
    }
    point as i32
}