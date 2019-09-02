import React, { Component } from 'react';
import ArticleBlock from "../../components/ArticleBlock/ArticleBlock";
import { listArticle } from "../../interfaces/ariticle"

export default class componentName extends Component {

    state = {
        data:[]
    }

    componentDidMount(){
        this.getArticle(1)

    }

    getArticle(pageNum){
        listArticle(pageNum).then(res=>{
            console.log(res)
            this.setState({
                data:res.data.result
            })
        })
        .catch(err => {
            console.log(err)
        })
    }

    render() {
        return (
            <div className="ariticles" style={{height:"100%",overflowY:"scroll"}}>
                {
                    this.state.data.map((item,index)=>{
                        return <ArticleBlock key={item.id} to={"/article/"+item.id} {...item}/>
                    })
                }
            </div>
        )
    }
}